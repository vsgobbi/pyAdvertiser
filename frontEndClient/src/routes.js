import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import Advertiser from "./pages/Advertiser";
import Dashboard from "./pages/Dashboard";

const Routes = () => (
  <BrowserRouter>
    <Switch>
      <Route exact path="/" component={Dashboard} />
      <Route path="/anunciante" component={Advertiser} />
    </Switch>
  </BrowserRouter>
);

export default Routes;