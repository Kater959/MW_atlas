import type { CadNodeLabel, CadViewAngle } from "@/content/types";

interface FixtureWireframeProps {
  view: CadViewAngle;
  rotation: number;
  nodes: CadNodeLabel[];
}

const VIEW_PRESETS: Record<
  CadViewAngle,
  { rotateX: number; rotateY: number; scaleY: number }
> = {
  front: { rotateX: 0, rotateY: 0, scaleY: 1 },
  top: { rotateX: 62, rotateY: 0, scaleY: 0.4 },
  iso: { rotateX: 18, rotateY: 28, scaleY: 0.9 },
};

export function FixtureWireframe({
  view,
  rotation,
  nodes,
}: FixtureWireframeProps) {
  const preset = VIEW_PRESETS[view];

  return (
    <div className="absolute inset-0 flex items-center justify-center">
      <div
        className="relative h-[72%] w-[72%] transition-transform duration-300 ease-out"
        style={{
          transform: `perspective(900px) rotateX(${preset.rotateX}deg) rotateY(${preset.rotateY + rotation * 0.15}deg) scaleY(${preset.scaleY})`,
          transformStyle: "preserve-3d",
        }}
      >
        <svg viewBox="0 0 200 140" className="h-full w-full" aria-hidden>
          <polygon
            points="20,110 180,110 175,125 25,125"
            fill="none"
            stroke="var(--border-edge)"
            strokeWidth="1.2"
          />
          <line
            x1="25"
            y1="110"
            x2="25"
            y2="125"
            stroke="var(--border-edge)"
            strokeWidth="1"
            opacity="0.6"
          />
          <line
            x1="180"
            y1="110"
            x2="175"
            y2="125"
            stroke="var(--border-edge)"
            strokeWidth="1"
            opacity="0.6"
          />
          <polygon
            points="45,75 155,75 150,105 50,105"
            fill="none"
            stroke="var(--border-edge)"
            strokeWidth="1.2"
          />
          <line
            x1="45"
            y1="75"
            x2="50"
            y2="105"
            stroke="var(--border-edge)"
            strokeWidth="1"
            opacity="0.5"
          />
          <line
            x1="155"
            y1="75"
            x2="150"
            y2="105"
            stroke="var(--border-edge)"
            strokeWidth="1"
            opacity="0.5"
          />
          <polygon
            points="70,55 130,55 128,72 72,72"
            fill="rgba(107, 125, 143, 0.06)"
            stroke="var(--accent-steel)"
            strokeWidth="1"
          />
          <line
            x1="60"
            y1="50"
            x2="60"
            y2="78"
            stroke="var(--border-edge)"
            strokeWidth="1.2"
          />
          <line
            x1="140"
            y1="50"
            x2="140"
            y2="78"
            stroke="var(--border-edge)"
            strokeWidth="1.2"
          />
          <line
            x1="55"
            y1="50"
            x2="65"
            y2="50"
            stroke="var(--border-edge)"
            strokeWidth="1.2"
          />
          <line
            x1="135"
            y1="50"
            x2="145"
            y2="50"
            stroke="var(--border-edge)"
            strokeWidth="1.2"
          />
          <line
            x1="100"
            y1="72"
            x2="100"
            y2="95"
            stroke="var(--accent-steel)"
            strokeWidth="1"
            strokeDasharray="3 2"
          />
          <line
            x1="68"
            y1="72"
            x2="68"
            y2="95"
            stroke="var(--accent-steel)"
            strokeWidth="1"
            strokeDasharray="3 2"
          />
          <line
            x1="132"
            y1="72"
            x2="132"
            y2="95"
            stroke="var(--accent-steel)"
            strokeWidth="1"
            strokeDasharray="3 2"
          />
          <line
            x1="50"
            y1="105"
            x2="45"
            y2="75"
            stroke="var(--border-edge)"
            strokeWidth="0.8"
            opacity="0.35"
            strokeDasharray="4 3"
          />
          <line
            x1="150"
            y1="105"
            x2="155"
            y2="75"
            stroke="var(--border-edge)"
            strokeWidth="0.8"
            opacity="0.35"
            strokeDasharray="4 3"
          />
        </svg>

        {nodes.map((node) => (
          <NodeCallout key={node.id} node={node} />
        ))}
      </div>
    </div>
  );
}

function NodeCallout({ node }: { node: CadNodeLabel }) {
  return (
    <div
      className="pointer-events-none absolute"
      style={{
        left: `${node.x}%`,
        top: `${node.y}%`,
        transform: "translate(-50%, -50%)",
      }}
    >
      <div className="flex items-center gap-1.5">
        <span className="h-1.5 w-1.5 shrink-0 rounded-full bg-[var(--accent-steel)]" />
        <span className="whitespace-nowrap font-mono text-[8px] tracking-widest text-[var(--text-mono)] uppercase sm:text-[9px]">
          {node.label}
        </span>
      </div>
    </div>
  );
}
