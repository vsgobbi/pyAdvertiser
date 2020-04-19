import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import Advertiser from "./pages/Advertiser";
import Dashboard from "./pages/Dashboard";
import Advertisement from "./pages/Advertisement";

const Routes = () => (
  <BrowserRouter>
    <Switch>
      <Route exact path="/" component={Dashboard} />
      <Route path="/cadastrarAnunciante" component={Advertiser} />
      <Route path="/cadastrarAnuncio" component={Advertisement} />
    </Switch>
  </BrowserRouter>
);

export default Routes;