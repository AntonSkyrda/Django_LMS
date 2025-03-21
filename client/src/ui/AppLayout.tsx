import { Outlet } from "react-router-dom";

export default function AppLayout() {
  return (
    <div className="grid h-[100dvh] w-16 grid-cols-1 grid-rows-2 bg-amber-400">
      <Outlet />
    </div>
  );
}
