import axios from "axios";
import { parseJwt } from "../config/jwtutils";

const LOGIN_URL = "http://127.0.0.1:8000/users/token/";
const REFRESH_URL = "http://127.0.0.1:8000/users/token/refresh/";

// Inicia sesión y guarda tokens
export const login = async (email, password) => {
  const response = await axios.post(LOGIN_URL, { email, password });
  if (response.data.access) {
    localStorage.setItem("accessToken", response.data.access);
    localStorage.setItem("refreshToken", response.data.refresh);
    //localStorage.setItem("currentUserId", response.data.user.id);

    const payload = parseJwt(response.data.access);
    if (payload?.user_id) {
      localStorage.setItem("currentUserId", payload.user_id.toString());
    }
    
  }
  return response.data;
};

// Cierra sesión
export const logout = () => {
  localStorage.removeItem("accessToken");
  localStorage.removeItem("refreshToken");
  window.location.reload();
};

// Refresca el accessToken si ha expirado
export const getAccessToken = async () => {
  let accessToken = localStorage.getItem("accessToken");
  const refreshToken = localStorage.getItem("refreshToken");

  try {
    // Hacemos una prueba real con un endpoint que SÍ permite GET con token (ej. el de usuarios)
    await axios.get("http://127.0.0.1:8000/users/api/", {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });
  } catch (error) {
    if (error.response?.status === 401 && refreshToken) {
      try {
        const response = await axios.post(REFRESH_URL, {
          refresh: refreshToken,
        });
        accessToken = response.data.access;
        localStorage.setItem("accessToken", accessToken);
      } catch (refreshError) {
        console.error("No se pudo refrescar el token:", refreshError);
        logout(); // Cerrar sesión si falla el refresh
      }
    }
  }

  return accessToken;
};