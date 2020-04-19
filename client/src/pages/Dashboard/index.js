import React, { Component } from "react";

import {Container } from "./styles";

class Dashboard extends Component {
  state = {
    taxId: "",
    fullName: "",
    companyName: "",
    phoneNumber: "",
    error: ""
  };

  handleSignUp = e => {
    e.preventDefault();
    alert("Eu vou te registrar");
  };

  render() {
    return (
      <Container>
       <div id="search">
          <input
            type="text"
            placeholder="Pesquisar por nome ou categoria"
          />
          <button>Buscar</button>
        </div>

      <div id="app">
        <main>
          <ul>
              <li className="dash-item">
                <header>
                  <img src="http://www.omsistemas.com/wp-content/uploads/2016/10/logotipo-om-negativo.png" alt="Teste" />
                    <div className="user-info">
                      <strong>OMSistemas</strong>  
                      <span>Tecnologia da Informação</span>
                    </div>
                  </header>
                  <p>SOMOS UMA EMPRESA DE ADAMANTINA/SP E CULTIVAMOS UM GRANDE COMPROMISSO COM A GESTÃO INTELIGENTE DAS EMPRESAS</p>
                  <a href={`http://www.omsistemas.com/`}>Veja mais sobre a empresa</a>
              </li>
              <li className="dash-item">
                <header>
                  <img src="https://goodu.com.br/static/img/header-logo.png" alt="Teste" />
                    <div className="user-info">
                      <strong>Goodu</strong>  
                      <span>Provedor de Internet</span>
                    </div>
                  </header>
                  <p>As pessoas mais próximas das novidades do mundo. As empresas mais ágeis e estáveis conectadas às novas oportunidades de negócios</p>
                  <a href={`https://goodu.com.br/`}>Veja mais sobre a empresa</a>
              </li>
              <li className="dash-item">
                <header>
                  <img src="http://www.risso.com.br/assets/images/rodapelogo-309x110.png" alt="Teste" />
                    <div className="user-info">
                      <strong>Risso</strong>  
                      <span>Tramportadora</span>
                    </div>
                  </header>
                  <p>Transportadora Risso mantém junto a todos os funcionários e prestadores de serviços uma política de compromisso com seu crescimento e aperfeiçoamento constantes</p>
                  <a href={`http://www.risso.com.br/`}>Veja mais sobre a empresa</a>
              </li>
              <li className="dash-item">
                <header>
                  <img src="https://www.luminarlimpeza.com.br/content/library/images/Logo-Luminar.png" alt="Teste" />
                    <div className="user-info">
                      <strong>Luminar</strong>  
                      <span>Produtos de Limpeza</span>
                    </div>
                  </header>
                  <p>Fundada em 1994, a Luminar é uma indústria química de gestão familiar, cuja paixão é desenvolver, fabricar e fornecer produtos de limpeza de altíssimo desempenho</p>
                  <a href={`https://www.luminarlimpeza.com.br/`}>Veja mais sobre a empresa</a>
              </li>
          </ul>
        </main>
    </div>
    </Container>
    );
  }
}

export default Dashboard;