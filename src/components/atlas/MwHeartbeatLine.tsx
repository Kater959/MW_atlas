"use client";

export function MwHeartbeatLine({ className = "" }: { className?: string }) {
  const path =
    "M 0 150 H 175 L 210 150 L 240 58 L 285 230 L 330 58 L 365 150 H 550 L 590 150 L 625 220 L 660 150 L 695 220 L 730 150 H 820 L 850 150 L 880 36 L 912 264 L 946 150 H 1100";

  return (
    <svg
      viewBox="0 0 1100 300"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      className={className}
      role="img"
      aria-label="MW heartbeat line"
    >
      <path
        className="mw-heartbeat-path"
        d={path}
        stroke="#B4FF2E"
        strokeWidth="4"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}
