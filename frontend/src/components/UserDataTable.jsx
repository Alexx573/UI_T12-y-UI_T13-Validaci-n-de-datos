import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import axios from "axios";
import ActualizarUsuario from "./ActualizarUsuario";
import { getAccessToken } from "../services/authService";
import Swal from "sweetalert2"

const UserDataTable = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [editingUser, setEditingUser] = useState(null)
  const currentUserId = localStorage.getItem("currentUserId");

  const fetchData = async () => {
    try {
      const accessToken = await getAccessToken();
      const response = await axios.get("http://127.0.0.1:8000/users/api/", {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });
      setData(response.data);
      setLoading(false);
    } catch (error) {
      console.error("Error al cargar los datos:", error);
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleEditClick = (user) => {
    setEditingUser(user);
  };

  const handleUpdateUser = async (updatedUser) => {
    try {
      const accessToken = await getAccessToken();
      await axios.put(
        `http://127.0.0.1:8000/users/api/${updatedUser.id}/`,
        updatedUser,
        {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        }
      );
      Swal.fire("¡Actualizado!", "El usuario fue actualizado correctamente.", "success");
      setEditingUser(null);
      fetchData(); // Recargar lista
    } catch (error) {
      console.error("Error al actualizar usuario:", error);
      Swal.fire("Error", "No se pudo actualizar el usuario.", "error");
    }
  };

  const handleDeleteUser = async (user) => {
    if (user.id.toString() === currentUserId) {
      Swal.fire("Atención", "No puedes eliminar tu propio usuario.", "warning");
      return;
    }


    const confirmResult = await Swal.fire({
      title: `¿Eliminar a ${user.name}?`,
      text: "Esta acción no se puede deshacer",
      icon: "warning",
      showCancelButton: true,
      confirmButtonText: "Sí, eliminar",
      cancelButtonText: "Cancelar",
    });

    if (!confirmResult.isConfirmed) {
      Swal.fire("Cancelado", "El usuario no fue eliminado.", "info");
      return;
    }

    try {
      const accessToken = await getAccessToken();
      await axios.delete(`http://127.0.0.1:8000/users/api/${user.id}/`, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });
      Swal.fire("Eliminado", "El usuario fue eliminado correctamente.", "success");
      fetchData();
    } catch (error) {
      console.error("Error al eliminar usuario:", error);
      Swal.fire("Error", "No se pudo eliminar el usuario.", "error");
    }
  };

  const columns = [
    {
      name: "Nombre",
      selector: (row) => row.name,
      sortable: true,
    },
    {
      name: "Email",
      selector: (row) => row.email,
      sortable: true,
    },
    {
      name: "Teléfono",
      selector: (row) => row.tel,
    },
    {
      name: "Acciones",
      cell: (row) => (
        <span>
          <button
            className="btn btn-warning me-4"
            onClick={() => handleEditClick(row)}
          >
            <i className="bi bi-pencil"></i>
          </button>
          <button
            className="btn btn-danger"
            onClick={() => handleDeleteUser(row)}
          >
            <i className="bi bi-trash"></i>
          </button>
        </span>
      ),
    },
  ];

  return (
    <div>
      <h3>Tabla de usuarios</h3>
      <DataTable
        columns={columns}
        data={data}
        progressPending={loading}
        pagination
        highlightOnHover
        pointerOnHover
      />
      {editingUser && (
        <ActualizarUsuario
          user={editingUser}
          onClose={() => setEditingUser(null)}
          onSave={handleUpdateUser}
        />
      )}
    </div>
  );
};

export default UserDataTable;