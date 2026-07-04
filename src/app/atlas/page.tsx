"use client";

import { useCallback, useState } from "react";
import {
  atlasGraph,
  resolveDossier,
} from "@/content/atlas";
import { AtlasCanvas } from "@/components/atlas/AtlasCanvas";
import { AtlasDetailPanel } from "@/components/atlas/AtlasDetailPanel";
import { AtlasManifesto } from "@/components/atlas/AtlasManifesto";
import { AtlasTopNav } from "@/components/atlas/AtlasTopNav";

export default function AtlasPage() {
  const [selectedDirectionId, setSelectedDirectionId] = useState<string | null>(
    null,
  );
  const [expandedDirectionId, setExpandedDirectionId] = useState<string | null>(
    null,
  );
  const [selectedSubnodeId, setSelectedSubnodeId] = useState<string | null>(
    null,
  );

  const dossier = resolveDossier(selectedDirectionId, selectedSubnodeId);

  const handleSelectDirection = useCallback((directionId: string) => {
    setSelectedDirectionId(directionId);
    setExpandedDirectionId(directionId);
    setSelectedSubnodeId(null);
  }, []);

  const handleSelectSubnode = useCallback(
    (directionId: string, subnodeId: string) => {
      setSelectedDirectionId(directionId);
      setExpandedDirectionId(directionId);
      setSelectedSubnodeId(subnodeId);
    },
    [],
  );

  const handleSelectCore = useCallback(() => {
    setSelectedDirectionId(null);
    setExpandedDirectionId(null);
    setSelectedSubnodeId(null);
  }, []);

  const handleCloseDossier = useCallback(() => {
    setSelectedDirectionId(null);
    setExpandedDirectionId(null);
    setSelectedSubnodeId(null);
  }, []);

  return (
    <div className="flex h-dvh flex-col overflow-hidden bg-[var(--bg-deck)]">
      <AtlasTopNav />
      <div className="flex min-h-0 flex-1">
        <AtlasManifesto manifesto={atlasGraph.manifesto} />
        <div className="flex min-w-0 flex-1 overflow-hidden">
          <div className="min-w-0 flex-1 overflow-y-auto">
            <AtlasCanvas
              selection={{
                selectedDirectionId,
                expandedDirectionId,
                selectedSubnodeId,
              }}
              onSelectDirection={handleSelectDirection}
              onSelectSubnode={handleSelectSubnode}
              onSelectCore={handleSelectCore}
            />
          </div>
          {dossier && (
            <div className="flex shrink-0 lg:relative">
              <AtlasDetailPanel
                dossier={dossier}
                onClose={handleCloseDossier}
              />
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
