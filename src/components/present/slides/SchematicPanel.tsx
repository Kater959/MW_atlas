export function SchematicPanel({
  variant,
  className = "",
}: {
  variant: "before" | "after";
  className?: string;
}) {
  const isBefore = variant === "before";
  const stroke = isBefore ? "var(--text-muted)" : "var(--border-edge)";
  const opacity = isBefore ? 0.45 : 0.9;
  const dash = isBefore ? "6 4" : undefined;

  return (
    <svg
      viewBox="0 0 280 160"
      className={`aspect-[7/4] w-full rounded-sm border border-[var(--border-subtle)] bg-[var(--bg-panel)] ${className}`}
      aria-hidden
    >
      <rect
        x="40"
        y="110"
        width="200"
        height="12"
        fill="none"
        stroke={stroke}
        strokeWidth="1"
        strokeDasharray={dash}
        opacity={opacity}
      />
      <rect
        x="80"
        y="65"
        width="120"
        height="45"
        fill="none"
        stroke={stroke}
        strokeWidth="1"
        strokeDasharray={dash}
        opacity={opacity}
      />
      <line
        x1="60"
        y1="65"
        x2="60"
        y2="122"
        stroke={stroke}
        strokeWidth="1"
        strokeDasharray={dash}
        opacity={opacity * 0.7}
      />
      <line
        x1="220"
        y1="65"
        x2="220"
        y2="122"
        stroke={stroke}
        strokeWidth="1"
        strokeDasharray={dash}
        opacity={opacity * 0.7}
      />
      {!isBefore && (
        <>
          <circle cx="60" cy="122" r="3" fill="var(--accent-steel)" />
          <circle cx="220" cy="122" r="3" fill="var(--accent-steel)" />
          <circle cx="140" cy="65" r="3" fill="var(--accent-steel)" />
        </>
      )}
    </svg>
  );
}
