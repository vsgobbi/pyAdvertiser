import React, { Component } from "react";
import { Form, Container } from "./styles";

class Advertiser extends Component {
  state = {
    taxId: "",
    fullName: "",
    companyName: "",
    phoneNumber: "",
    error: ""
  };

  handleSignUp = e => {
    e.preventDefault();
    alert("Anúncio cadastrado");
  };

  render() {
    return (
      <Container>
        <Form onSubmit={this.handleSignUp}>
          {this.state.error && <p>{this.state.error}</p>}
          <input
            type="text"
            placeholder="Título"
            onChange={e => this.setState({ fullName: e.target.value })}
          />
          <input
            type="text"
            placeholder="Descriçao"
            onChange={e => this.setState({ companyName: e.target.value })}
          />
          <input
            type="tel"
            placeholder="Telefone"
            onChange={e => this.setState({ phoneNumber: e.target.value })}
          />
          <input
            type="tel"
            placeholder="Telefone"
            onChange={e => this.setState({ phoneNumber: e.target.value })}
          />
          <button type="submit">Salvar</button>
        </Form>
      </Container>
    );
  }
}

export default Advertiser;