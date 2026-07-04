"use client";

import { MwHeartbeatLine } from "./MwHeartbeatLine";

export function PulseConnector({
  active = false,
  variant = "connector",
}: {
  active?: boolean;
  variant?: "connector" | "mw-intro";
}) {
  const lineClass = active
    ? "bg-[var(--accent-signal)] mw-pulse-line-active"
    : "bg-white/10";

  if (variant === "mw-intro") {
    return (
      <div
        className="flex w-full max-w-[320px] flex-col items-center"
        aria-hidden
      >
        <div className={`h-5 w-px ${lineClass}`} />
        <MwHeartbeatLine className="h-8 w-full opacity-95" />
        <div className={`h-8 w-px ${lineClass}`} />
      </div>
    );
  }

  return (
    <div className="flex flex-col items-center" aria-hidden>
      <div className={`h-11 w-px ${lineClass}`} />
    </div>
  );
}
