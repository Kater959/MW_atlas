import type { CadNodeLabel } from "@/content/types";
import { CadViewerPlaceholder } from "./CadViewerPlaceholder";

/**
 * Stable slot for CAD viewer. v0.1 renders placeholder; v0.2 swaps in GLB/lambda360view.
 */
export interface CadViewerSlotProps {
  model: ArrayBuffer | string | null;
  nodes: CadNodeLabel[];
  footer: string;
  compact?: boolean;
}

export function CadViewerSlot({
  model,
  nodes,
  footer,
  compact = false,
}: CadViewerSlotProps) {
  if (model) {
    // v0.2: mount real viewer here (lambda360view / R3F)
    return (
      <CadViewerPlaceholder nodes={nodes} footer={footer} compact={compact} />
    );
  }

  return (
    <CadViewerPlaceholder nodes={nodes} footer={footer} compact={compact} />
  );
}
