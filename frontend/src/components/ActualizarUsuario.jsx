import React, { useState } from "react";
import Swal from "sweetalert2";


const ActualizarUsuario = ({ user, onClose, onSave }) => {
  const [formData, setFormData] = useState({ ...user });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = () => {
    Swal.fire({
      title: "¿Guardar cambios?",
      text: "Se actualizará la información del usuario.",
      icon: "question",
      showCancelButton: true,
      confirmButtonText: "Sí, guardar",
      cancelButtonText: "Cancelar",
    }).then((result) => {
      if (result.isConfirmed) {
        onSave(formData);
      } else {
        Swal.fire("Cancelado", "No se guardaron los cambios.", "info");
      }
    });
  };
  if (!user) return null;

  console.log(formData);
  

  return (
    <div className="modal show d-block" tabIndex="-1" role="dialog">
      <div className="modal-dialog" role="document">
        <div className="modal-content p-3">
          <h5 className="modal-title">Editar Usuario</h5>
          <div className="modal-body">
            <input
              className="form-control mb-2"
              name="name"
              value={formData.name}
              onChange={handleChange}
              placeholder="Nombre"
            />
            <input
              className="form-control mb-2"
              name="surname"
              value={formData.surname}
              onChange={handleChange}
              placeholder="Apellido"
            />
             <input
              className="form-control mb-2"
              name="age"
              value={formData.age}
              onChange={handleChange}
              placeholder="Edad"
            />
             <input
              className="form-control mb-2"
              name="control_number"
              value={formData.control_number}
              onChange={handleChange}
              placeholder="Matricula"
            />
            <input
              className="form-control mb-2"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="Correo"
            />
            <input
              className="form-control mb-2"
              name="tel"
              value={formData.tel}
              onChange={handleChange}
              placeholder="Teléfono"
            />
          </div>
          <div className="modal-footer">
            <button className="btn btn-secondary" onClick={onClose}>
              Cancelar
            </button>
            <button className="btn btn-primary" onClick={handleSubmit}>
              Guardar Cambios
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ActualizarUsuario;