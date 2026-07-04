"use client";

import { atlasGraph, getAtlasDirections, getAtlasRoot } from "@/content/atlas";
import { PULSE_TREE } from "./atlas-board-layout";
import {
  PulseCoreCard,
  RecoveryModuleCard,
  SubnodeBranch,
  SubnodeCard,
} from "./AtlasNode";
import { PulseConnector } from "./PulseConnector";

export interface PulseTreeSelection {
  selectedDirectionId: string | null;
  expandedDirectionId: string | null;
  selectedSubnodeId: string | null;
}

function displayTitleFor(title: string): string {
  const map: Record<string, string> = {
    "Станочная зажимная оснастка": "Станочная\nзажимная оснастка",
    "Подъёмные и монтажные приспособления":
      "Подъёмные и\nмонтажные приспособления",
    "Механизация ручных операций": "Механизация\nручных операций",
    "Контрольные приспособления": "Контрольные\nприспособления",
    "Нестандартное оборудование": "Нестандартное\nоборудование",
  };
  return map[title] ?? title;
}

function getDirectionIndex(directionId: string | null): number {
  if (!directionId) return -1;
  return getAtlasDirections().findIndex((d) => d.id === directionId);
}

export interface AtlasCanvasProps {
  selection: PulseTreeSelection;
  onSelectDirection: (directionId: string) => void;
  onSelectSubnode: (directionId: string, subnodeId: string) => void;
  onSelectCore: () => void;
}

export function AtlasCanvas({
  selection,
  onSelectDirection,
  onSelectSubnode,
  onSelectCore,
}: AtlasCanvasProps) {
  const root = getAtlasRoot();
  const directions = getAtlasDirections();
  const manifesto = atlasGraph.manifesto;
  const { selectedDirectionId, expandedDirectionId, selectedSubnodeId } =
    selection;

  const activeDirectionIndex = getDirectionIndex(expandedDirectionId);
  const hasExpandedBranch = expandedDirectionId !== null;

  return (
    <div className="pulse-tree snap-grid relative min-h-full w-full bg-[var(--bg-deck)]">
      <div
        className="relative mx-auto flex flex-col items-center px-6 py-12 pb-24"
        style={{ maxWidth: PULSE_TREE.maxContentWidth }}
      >
        <div
          className="pointer-events-none absolute top-[120px] bottom-12 left-1/2 w-px -translate-x-1/2 bg-white/[0.06]"
          aria-hidden
        />

        <PulseCoreCard
          label={manifesto.centerTitle}
          tagline={manifesto.centerTagline}
          exploreLabel={manifesto.exploreLabel}
          selected={false}
          onClick={onSelectCore}
        />

        <PulseConnector
          variant="mw-intro"
          active={activeDirectionIndex >= 0}
        />

        {directions.map((direction, index) => {
          const isExpanded = expandedDirectionId === direction.id;
          const isSelectedDirection = selectedDirectionId === direction.id;
          const isDimmed =
            hasExpandedBranch && expandedDirectionId !== direction.id;
          const subnodes = direction.subnodes ?? [];
          const showBranch = isExpanded && subnodes.length > 0;

          return (
            <div key={direction.id} className="flex w-full flex-col items-center">
              <RecoveryModuleCard
                ref={direction.ref}
                title={direction.title}
                displayTitle={displayTitleFor(direction.title)}
                hook={direction.strongPhrase}
                moduleLabel="Recovery Module"
                selected={isSelectedDirection && !selectedSubnodeId}
                expanded={isExpanded}
                dimmed={isDimmed}
                onClick={() => onSelectDirection(direction.id)}
              />

              {showBranch && (
                <>
                  <PulseConnector active />
                  <SubnodeBranch active={isSelectedDirection}>
                    {subnodes.map((subnode, subIndex) => (
                      <SubnodeCard
                        key={subnode.id}
                        title={subnode.title}
                        hook={subnode.strongPhrase}
                        subnodeType={subnode.type}
                        selected={
                          selectedSubnodeId === subnode.id &&
                          selectedDirectionId === direction.id
                        }
                        dimmed={
                          selectedSubnodeId !== null &&
                          selectedSubnodeId !== subnode.id
                        }
                        isLast={subIndex === subnodes.length - 1}
                        onClick={() =>
                          onSelectSubnode(direction.id, subnode.id)
                        }
                      />
                    ))}
                  </SubnodeBranch>
                </>
              )}

              {index < directions.length - 1 && (
                <PulseConnector active={activeDirectionIndex > index} />
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
