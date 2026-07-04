"use client";

import { useCallback, useRef, useState } from "react";
import type { CadNodeLabel, CadViewAngle } from "@/content/types";
import { FixtureWireframe } from "./FixtureWireframe";

const VIEW_TABS: { id: CadViewAngle; label: string }[] = [
  { id: "front", label: "FRONT" },
  { id: "top", label: "TOP" },
  { id: "iso", label: "ISO" },
];

export interface CadViewerPlaceholderProps {
  nodes: CadNodeLabel[];
  footer: string;
  compact?: boolean;
}

export function CadViewerPlaceholder({
  nodes,
  footer,
  compact = false,
}: CadViewerPlaceholderProps) {
  const [view, setView] = useState<CadViewAngle>("iso");
  const [rotation, setRotation] = useState(0);
  const [isDragging, setIsDragging] = useState(false);
  const dragStart = useRef({ x: 0, angle: 0 });

  const onPointerDown = useCallback(
    (event: React.PointerEvent) => {
      setIsDragging(true);
      dragStart.current = { x: event.clientX, angle: rotation };
      event.currentTarget.setPointerCapture(event.pointerId);
    },
    [rotation],
  );

  const onPointerMove = useCallback(
    (event: React.PointerEvent) => {
      if (!isDragging) return;
      const delta = event.clientX - dragStart.current.x;
      setRotation(dragStart.current.angle + delta * 0.4);
    },
    [isDragging],
  );

  const onPointerUp = useCallback(() => {
    setIsDragging(false);
  }, []);

  return (
    <div
      className={`corner-brackets corner-brackets-inner engineering-grid rounded-sm border border-[var(--border-subtle)] bg-[var(--bg-panel)] ${compact ? "p-3" : "p-4 sm:p-6"}`}
    >
      <div className="mb-4 flex flex-wrap items-center justify-between gap-4">
        <span className="font-mono text-[10px] tracking-[0.2em] text-[var(--text-mono)] uppercase">
          CAD VIEWER
        </span>
        <div className="flex gap-1">
          {VIEW_TABS.map((tab) => (
            <button
              key={tab.id}
              type="button"
              onClick={() => setView(tab.id)}
              className={`px-3 py-1.5 font-mono text-[10px] tracking-widest uppercase transition-colors ${
                view === tab.id
                  ? "border border-[var(--accent-steel)] text-[var(--text-primary)]"
                  : "border border-transparent text-[var(--text-muted)] hover:text-[var(--text-mono)]"
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>
      </div>

      <div
        className={`relative w-full cursor-grab overflow-hidden rounded-sm border border-[var(--border-subtle)] bg-[var(--bg-deck)] active:cursor-grabbing ${compact ? "aspect-[4/3]" : "aspect-[16/10]"}`}
        onPointerDown={onPointerDown}
        onPointerMove={onPointerMove}
        onPointerUp={onPointerUp}
        onPointerLeave={onPointerUp}
        role="img"
        aria-label="CAD placeholder. Перетащите для вращения."
      >
        <FixtureWireframe view={view} rotation={rotation} nodes={nodes} />
      </div>

      <ul className="mt-4 grid gap-2 border-t border-[var(--border-subtle)] pt-4 sm:grid-cols-2 lg:grid-cols-3">
        {nodes.map((node) => (
          <li key={node.id} className="font-mono text-[10px] text-[var(--text-muted)]">
            <span className="tracking-widest text-[var(--text-mono)] uppercase">
              {node.label}
            </span>
            <span className="text-[var(--text-muted)]"> — {node.description}</span>
          </li>
        ))}
      </ul>

      <footer className="mt-4 flex items-center justify-between gap-4 border-t border-[var(--border-subtle)] pt-4">
        <p className="font-mono text-[10px] tracking-widest text-[var(--text-muted)]">
          {footer}
        </p>
        <p className="font-mono text-[10px] text-[var(--text-muted)]">
          drag to rotate
        </p>
      </footer>
    </div>
  );
}
