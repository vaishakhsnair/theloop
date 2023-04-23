import './App.css';
import Chart from "chart.js/auto";

import { BrowserRouter, Routes, Route } from "react-router-dom";
import SignInPage from './pages/login'
import AdminPage from './pages/admin'
import { CategoryScale } from "chart.js";

Chart.register(CategoryScale);



function App() {
  

  return (
    <div className="App">

      <BrowserRouter>
      <Routes>
      <Route path="/" element={SignInPage()}></Route>
      <Route path="/admin" element={AdminPage()}></Route>

x      </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
