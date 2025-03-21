declare global {
  namespace NodeJS {
    interface ProcessEnv {
      VITE_BASE_URL: string;
      ENV: "test" | "dev" | "prod";
    }
  }
}

export {};
