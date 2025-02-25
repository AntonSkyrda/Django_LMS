import { createContext, useContext, useState, useEffect } from "react";
import { login as loginService, logout as logoutService } from "../services/authService";

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (token) {
      setUser({ isAuthenticated: true });
    }
  }, []);

  const login = async (email, password) => {
    await loginService(email, password);
    setUser({ isAuthenticated: true });
  };

  const logout = () => {
    logoutService();
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
