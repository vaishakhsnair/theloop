import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import SignInPage from './pages/login'
import adminPage from './pages/admin'

function App() {
  return (
    <div className="App">

      <BrowserRouter>
      <Routes>
        <Route path="/login" element={SignInPage()}></Route>
        <Route path="/admin" element={adminPage()}></Route>

x      </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
