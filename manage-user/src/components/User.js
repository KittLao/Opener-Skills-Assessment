import React from "react";

export class User extends React.Component {
  getStyle = () => {
    return {
      background: "#f4f4f4",
      padding: "10px",
      borderBottom: "1px #ccc dotted",
    };
  };

    render() {
        const { id, name, email, phoneNumber, department, showAll } = this.props.user;
        const toggleDetailsOf = this.props.toggleDetailsOf;
        return (
            <div style={this.getStyle()}>
                {
                    !showAll ? (
                        <div>
                            <div>
                                <p> Name: {name}</p>
                            </div>
                            <button style={btnStyle} onClick={() => toggleDetailsOf(id)}>
                                Show details 
                            </button>
                        </div>
                    ) : (
                        <div>
                            <div>
                                <p> Name: {name}</p>
                                <p> Email: {email} </p>
                                <p> Phone Number: {phoneNumber} </p>
                                <p> Department: {department} </p>
                            </div>
                            <button style={btnStyle} onClick={() => toggleDetailsOf(id)}>
                                Hide details 
                            </button>
                        </div>
                    )
                }
            </div>
        );
    }
}

const btnStyle = {
//   background: "#ff0000",
//   color: "#fff",
  border: "none",
  padding: "5px 9px",
  cursor: "pointer",
  float: "right",
};

export default User;