"use client";

import type { AtlasSubnodeType } from "@/content/atlas-types";

const SUBNODE_TYPE_LABEL: Partial<Record<AtlasSubnodeType, string>> = {
  solutionType: "Solution Type",
  pain: "Symptom Map",
  data: "Input Data",
  whereUsed: "Application Zone",
  cad: "CAD Node",
};

export function PulseCoreCard({
  label,
  tagline,
  exploreLabel,
  selected,
  onClick,
}: {
  label: string;
  tagline?: string;
  exploreLabel?: string;
  selected?: boolean;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={`relative w-full border bg-[var(--bg-panel)] px-10 py-10 text-left transition-colors duration-200 ${
        selected
          ? "border-[var(--accent-signal)] shadow-[0_0_0_1px_rgba(180,255,46,0.2)]"
          : "border-[var(--border-subtle)] hover:border-[var(--border-edge)]"
      }`}
    >
      <span className="mb-6 inline-block h-[3px] w-10 bg-[var(--accent-signal)]" />
      <p className="text-4xl font-semibold tracking-[-0.04em] text-[var(--text-primary)] uppercase lg:text-5xl">
        {label}
      </p>
      {tagline && (
        <p className="mt-6 text-lg leading-relaxed text-[var(--text-muted)]">
          {tagline}
        </p>
      )}
      {exploreLabel && (
        <p className="mt-10 font-mono text-[11px] tracking-[0.25em] text-[var(--accent-signal)] uppercase">
          {exploreLabel}
        </p>
      )}
    </button>
  );
}

export function RecoveryModuleCard({
  ref: moduleRef,
  title,
  displayTitle,
  hook,
  moduleLabel,
  selected,
  expanded,
  dimmed,
  onClick,
}: {
  ref?: string;
  title: string;
  displayTitle?: string;
  hook?: string;
  moduleLabel?: string;
  selected?: boolean;
  expanded?: boolean;
  dimmed?: boolean;
  onClick: () => void;
}) {
  const isActive = selected || expanded;

  return (
    <button
      type="button"
      onClick={onClick}
      className={`group relative w-full border bg-[var(--bg-panel)] px-6 py-6 text-left transition-all duration-300 ${
        isActive
          ? "border-[var(--accent-signal)] shadow-[0_0_0_1px_rgba(180,255,46,0.15)]"
          : "border-[var(--border-subtle)] hover:border-[var(--border-edge)]"
      } ${dimmed ? "opacity-40 saturate-50" : "opacity-100"}`}
    >
      {moduleRef && (
        <p className="font-mono text-[11px] tracking-[0.2em] text-[var(--accent-signal)] uppercase">
          {moduleRef}
          {moduleLabel && (
            <span className="text-[var(--text-dim)]"> · {moduleLabel}</span>
          )}
        </p>
      )}
      <h3 className="mt-3 text-xl font-semibold leading-[1.15] tracking-[-0.02em] text-[var(--text-primary)] uppercase whitespace-pre-line">
        {displayTitle ?? title}
      </h3>
      {hook && (
        <p className="mt-4 text-sm leading-relaxed text-[var(--text-muted)]">
          {hook}
        </p>
      )}
      <span
        className={`mt-6 inline-block font-mono text-lg transition-colors ${
          isActive
            ? "text-[var(--accent-signal)]"
            : "text-[var(--text-dim)] group-hover:text-[var(--accent-signal)]"
        }`}
      >
        {expanded ? "▾" : "↓"}
      </span>
    </button>
  );
}

export function SubnodeCard({
  title,
  hook,
  subnodeType,
  selected,
  dimmed,
  isLast,
  onClick,
}: {
  title: string;
  hook?: string;
  subnodeType?: AtlasSubnodeType;
  selected?: boolean;
  dimmed?: boolean;
  isLast?: boolean;
  onClick: () => void;
}) {
  const typeLabel = subnodeType ? SUBNODE_TYPE_LABEL[subnodeType] : undefined;

  return (
    <div className="relative flex w-full pl-8">
      <div
        className={`absolute top-0 left-[15px] w-px ${
          isLast ? "h-1/2" : "bottom-0"
        } ${selected ? "bg-[var(--accent-signal)]" : "bg-white/10"}`}
        aria-hidden
      />
      <div
        className={`absolute top-1/2 left-[15px] h-px w-5 -translate-y-1/2 ${
          selected ? "bg-[var(--accent-signal)]" : "bg-white/10"
        }`}
        aria-hidden
      />

      <button
        type="button"
        onClick={onClick}
        className={`relative ml-5 w-[calc(100%-20px)] border bg-[var(--bg-panel)] px-5 py-4 text-left transition-all duration-200 ${
          selected
            ? "border-[var(--accent-signal)] shadow-[0_0_0_1px_rgba(180,255,46,0.12)]"
            : "border-[var(--border-subtle)] hover:border-[var(--border-edge)]"
        } ${dimmed ? "opacity-45" : "opacity-100"}`}
      >
        {typeLabel && (
          <p className="font-mono text-[9px] tracking-[0.2em] text-[var(--text-dim)] uppercase">
            {typeLabel}
          </p>
        )}
        <h4 className="mt-1 text-base font-semibold leading-snug tracking-[-0.02em] text-[var(--text-primary)] uppercase">
          {title}
        </h4>
        {hook && (
          <p className="mt-2 line-clamp-2 text-xs leading-relaxed text-[var(--text-muted)]">
            {hook}
          </p>
        )}
      </button>
    </div>
  );
}

export function SubnodeBranch({
  children,
  active,
}: {
  children: React.ReactNode;
  active?: boolean;
}) {
  return (
    <div
      className={`relative w-full py-2 transition-opacity duration-300 ${
        active ? "opacity-100" : "opacity-100"
      }`}
    >
      <div
        className={`absolute top-0 bottom-0 left-[15px] w-px ${
          active ? "bg-[var(--accent-signal)]/40" : "bg-white/[0.06]"
        }`}
        aria-hidden
      />
      <div className="flex flex-col gap-3">{children}</div>
    </div>
  );
}
