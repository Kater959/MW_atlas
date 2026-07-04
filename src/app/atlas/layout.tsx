import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Metalwork Pulse",
  description:
    "Реанимация для больных производственных операций — инженерная диагностика Metalwork",
};

export default function AtlasLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return children;
}
