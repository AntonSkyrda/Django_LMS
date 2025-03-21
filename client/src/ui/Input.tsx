import { ComponentPropsWithoutRef } from "react";
import { cn } from "../lib/utils/cn";

interface InputProps extends ComponentPropsWithoutRef<"input"> {
  additionalStyles?: string;
}

export default function Input({ additionalStyles, ...props }: InputProps) {
  const styles =
    "rounded-sm border border-gray-300 bg-gray-50 px-5 py-3 shadow-sm";

  return <input className={cn(styles, additionalStyles)} {...props} />;
}
