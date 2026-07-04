import type { AtlasManifesto as AtlasManifestoType } from "@/content/atlas-types";
import { MwHeartbeatLine } from "./MwHeartbeatLine";

export function AtlasManifesto({
  manifesto,
}: {
  manifesto: AtlasManifestoType;
}) {
  return (
    <aside className="atlas-manifesto atlas-manifesto-compact hidden h-full w-[clamp(420px,34vw,520px)] shrink-0 flex-col justify-between overflow-hidden border-r border-[var(--border-subtle)] bg-[var(--bg-deck)] px-8 py-8 lg:flex lg:px-10 lg:py-10 xl:py-12">
      <div className="atlas-manifesto-scroll min-h-0 flex-1 overflow-x-visible">
        <p className="font-mono text-[11px] tracking-[0.28em] text-[var(--text-dim)] uppercase">
          Metalwork Pulse
        </p>
        <p className="mt-2 font-mono text-[11px] tracking-[0.2em] text-[var(--accent-signal)] uppercase">
          Engineering Diagnostic Canvas
        </p>

        <div className="atlas-manifesto-pulse-block mt-8 lg:mt-10">
          <p className="text-[length:var(--atlas-sub)] font-semibold tracking-[-0.03em] text-[var(--text-primary)] uppercase">
            {manifesto.productTitle}
          </p>
          <p className="mt-1 text-[length:var(--atlas-hero)] leading-[1.05] font-semibold tracking-[-0.03em] text-[var(--accent-signal)] uppercase">
            {manifesto.productPulse}
          </p>
          <div className="mt-5 w-full lg:mt-6">
            <MwHeartbeatLine className="h-10 w-full" />
          </div>
          <p className="mt-5 max-w-[36ch] text-[0.9375rem] leading-relaxed text-[var(--text-muted)] lg:mt-6 lg:text-base">
            {manifesto.pulseLead}
          </p>
        </div>

        <h1 className="atlas-editorial-hero-wrap atlas-editorial-hero mt-10 font-semibold text-[var(--text-primary)] uppercase lg:mt-12">
          ОТК НЕ
          <br />
          ПРЕДОТВРАЩАЕТ
          <br />
          БРАК.
          <br />
          <span className="text-[var(--accent-signal)]">
            ОН
            <br />
            ФИКСИРУЕТ
            <br />
            УБЫТКИ.
          </span>
        </h1>

        <p className="atlas-editorial-subline mt-6 max-w-[34ch] text-[length:var(--atlas-sub)] leading-relaxed text-[var(--text-muted)] lg:mt-8">
          {manifesto.editorialSubline}
        </p>
      </div>

      <p className="mt-4 shrink-0 font-mono text-[10px] leading-relaxed tracking-widest text-[var(--text-dim)] uppercase">
        Scroll · recovery modules
      </p>
    </aside>
  );
}
