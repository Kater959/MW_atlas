"use client";

import Link from "next/link";
import type { AtlasSubnode } from "@/content/atlas-types";
import type { DossierTarget } from "@/content/atlas";
import { clampingFixturesCadLabels } from "@/content/atlas";
import { CadViewerSlot } from "@/components/cad/CadViewerSlot";
import { EngineeringVisualCard } from "./EngineeringVisualCard";

export interface AtlasDetailPanelProps {
  dossier: DossierTarget;
  onClose: () => void;
}

export function AtlasDetailPanel({ dossier, onClose }: AtlasDetailPanelProps) {
  if (dossier.kind === "subnode") {
    return (
      <DossierShell
        ref={dossier.direction.ref}
        directionTitle={dossier.direction.title}
        title={dossier.subnode.title}
        subnodeType={dossier.subnode.type}
        onClose={onClose}
        cta={dossier.direction.cta}
        directionRoute={dossier.direction.directionRoute}
        presentRoute={dossier.direction.presentRoute}
      >
        <SubnodeDossierContent
          subnode={dossier.subnode}
          directionId={dossier.direction.id}
        />
      </DossierShell>
    );
  }

  const { direction: node } = dossier;
  const hasCadMedia =
    node.id === "clamping-fixtures" &&
    node.mediaPlan?.some((m) => m.type === "cad");

  return (
    <DossierShell
      ref={node.ref}
      title={node.title}
      onClose={onClose}
      cta={node.cta}
      directionRoute={node.directionRoute}
      presentRoute={node.presentRoute}
    >
      {node.strongPhrase && (
        <blockquote className="text-xl leading-snug font-medium text-[var(--text-primary)]">
          <span className="mr-2 text-[var(--accent-signal)]">—</span>
          {node.strongPhrase}
        </blockquote>
      )}

      {(node.summary || node.purpose) && (
        <p className="mt-6 text-base leading-relaxed text-[var(--text-muted)]">
          {node.summary}
          {node.purpose && (
            <>
              {" "}
              <span className="text-[var(--text-primary)]">{node.purpose}</span>
            </>
          )}
        </p>
      )}

      {node.subnodes && node.subnodes.length > 0 && (
        <p className="mt-6 font-mono text-[10px] tracking-[0.2em] text-[var(--accent-signal)] uppercase">
          ↓ Выберите узел в pulse-tree для детализации
        </p>
      )}

      {node.painPoints && node.painPoints.length > 0 && (
        <Section title="Симптом">
          <ul className="space-y-3">
            {node.painPoints.map((item) => (
              <li
                key={item}
                className="border-l-2 border-[var(--border-subtle)] pl-4 text-base text-[var(--text-muted)]"
              >
                {item}
              </li>
            ))}
          </ul>
        </Section>
      )}

      {((node.whereUsed && node.whereUsed.length > 0) ||
        (node.whenNotUsed && node.whenNotUsed.length > 0)) && (
        <Section title="Где теряется управление">
          {node.whereUsed && node.whereUsed.length > 0 && (
            <ul className="space-y-2">
              {node.whereUsed.map((item) => (
                <li key={item} className="text-base text-[var(--text-muted)]">
                  {item}
                </li>
              ))}
            </ul>
          )}
          {node.whenNotUsed && node.whenNotUsed.length > 0 && (
            <ul className="mt-4 space-y-2">
              {node.whenNotUsed.map((item) => (
                <li
                  key={item}
                  className="border-l-2 border-[var(--border-subtle)] pl-4 text-base text-[var(--text-muted)]"
                >
                  {item}
                </li>
              ))}
            </ul>
          )}
        </Section>
      )}

      {node.solutionTypes && node.solutionTypes.length > 0 && (
        <Section title="Инженерное восстановление">
          <ul className="space-y-4">
            {node.solutionTypes.map((item) => (
              <li
                key={item.title}
                className="border border-[var(--border-subtle)] bg-[var(--bg-deck)] p-5"
              >
                <p className="font-mono text-[11px] tracking-widest text-[var(--accent-signal)] uppercase">
                  {item.title}
                </p>
                <p className="mt-2 text-sm leading-relaxed text-[var(--text-muted)]">
                  {item.description}
                </p>
              </li>
            ))}
          </ul>
        </Section>
      )}

      {node.questions && node.questions.length > 0 && (
        <Section title="Диагностические вопросы">
          <ul className="space-y-4">
            {node.questions.map((item) => (
              <li
                key={item}
                className="text-base leading-relaxed text-[var(--text-primary)]"
              >
                {item}
              </li>
            ))}
          </ul>
        </Section>
      )}

      {node.requiredInput && node.requiredInput.length > 0 && (
        <Section title="Что нужно для расчёта">
          <ul className="space-y-2">
            {node.requiredInput.map((item) => (
              <li
                key={item}
                className="font-mono text-sm text-[var(--text-mono)]"
              >
                {item}
              </li>
            ))}
          </ul>
        </Section>
      )}

      {hasCadMedia && (
        <Section title="CAD viewer">
          <CadViewerSlot
            model={null}
            nodes={clampingFixturesCadLabels}
            footer="PLACEHOLDER · GLB INTEGRATION v0.2"
            compact
          />
        </Section>
      )}

      {node.type === "direction" &&
        !node.painPoints &&
        !node.subnodes?.length && (
          <p className="mt-10 font-mono text-[11px] tracking-widest text-[var(--text-dim)] uppercase">
            Полный dossier — в разработке
          </p>
        )}
    </DossierShell>
  );
}

function SubnodeDossierContent({
  subnode,
  directionId,
}: {
  subnode: AtlasSubnode;
  directionId: string;
}) {
  const showCad =
    subnode.type === "cad" && directionId === "clamping-fixtures";

  return (
    <>
      {subnode.strongPhrase && (
        <blockquote className="text-xl leading-snug font-medium text-[var(--text-primary)]">
          <span className="mr-2 text-[var(--accent-signal)]">—</span>
          {subnode.strongPhrase}
        </blockquote>
      )}

      {subnode.summary && (
        <Section title="Что это">
          <p className="text-base leading-relaxed text-[var(--text-muted)]">
            {subnode.summary}
          </p>
        </Section>
      )}

      {subnode.purpose && (
        <Section title="Зачем нужно">
          <p className="text-base leading-relaxed text-[var(--text-primary)]">
            {subnode.purpose}
          </p>
        </Section>
      )}

      {subnode.painPoints && subnode.painPoints.length > 0 && (
        <Section title="Симптом">
          <ul className="space-y-3">
            {subnode.painPoints.map((item) => (
              <li
                key={item}
                className="border-l-2 border-[var(--border-subtle)] pl-4 text-base text-[var(--text-muted)]"
              >
                {item}
              </li>
            ))}
          </ul>
        </Section>
      )}

      {subnode.whereUsed && subnode.whereUsed.length > 0 && (
        <Section title="Где применять">
          <ul className="space-y-2">
            {subnode.whereUsed.map((item) => (
              <li key={item} className="text-base text-[var(--text-muted)]">
                {item}
              </li>
            ))}
          </ul>
        </Section>
      )}

      {subnode.whenToUse && subnode.whenToUse.length > 0 && (
        <Section title="Когда применять">
          <ul className="space-y-2">
            {subnode.whenToUse.map((item) => (
              <li key={item} className="text-base text-[var(--text-muted)]">
                {item}
              </li>
            ))}
          </ul>
        </Section>
      )}

      {subnode.whenNotToUse && subnode.whenNotToUse.length > 0 && (
        <Section title="Когда не применять">
          <ul className="space-y-2">
            {subnode.whenNotToUse.map((item) => (
              <li
                key={item}
                className="border-l-2 border-[var(--border-subtle)] pl-4 text-base text-[var(--text-muted)]"
              >
                {item}
              </li>
            ))}
          </ul>
        </Section>
      )}

      {subnode.advantages && subnode.advantages.length > 0 && (
        <Section title="Преимущества">
          <ul className="space-y-2">
            {subnode.advantages.map((item) => (
              <li key={item} className="text-base text-[var(--text-primary)]">
                {item}
              </li>
            ))}
          </ul>
        </Section>
      )}

      {subnode.risks && subnode.risks.length > 0 && (
        <Section title="Риски">
          <ul className="space-y-2">
            {subnode.risks.map((item) => (
              <li key={item} className="text-base text-[var(--text-muted)]">
                {item}
              </li>
            ))}
          </ul>
        </Section>
      )}

      {subnode.questions && subnode.questions.length > 0 && (
        <Section title="Вопросы клиенту">
          <ul className="space-y-4">
            {subnode.questions.map((item) => (
              <li
                key={item}
                className="text-base leading-relaxed text-[var(--text-primary)]"
              >
                {item}
              </li>
            ))}
          </ul>
        </Section>
      )}

      {subnode.requiredInput && subnode.requiredInput.length > 0 && (
        <Section title="Что нужно для расчёта">
          <ul className="space-y-2">
            {subnode.requiredInput.map((item) => (
              <li
                key={item}
                className="font-mono text-sm text-[var(--text-mono)]"
              >
                {item}
              </li>
            ))}
          </ul>
        </Section>
      )}

      {subnode.visuals && subnode.visuals.length > 0 && (
        <Section title="Engineering Visual">
          <div className="space-y-6">
            {subnode.visuals.map((visual) => (
              <EngineeringVisualCard
                key={visual.id ?? visual.src}
                visual={visual}
              />
            ))}
          </div>
        </Section>
      )}

      {showCad && (
        <Section title="CAD / схема узлов">
          <CadViewerSlot
            model={null}
            nodes={clampingFixturesCadLabels}
            footer="PLACEHOLDER · GLB INTEGRATION v0.2"
            compact
          />
        </Section>
      )}
    </>
  );
}

function DossierShell({
  ref: dirRef,
  directionTitle,
  title,
  subnodeType,
  onClose,
  cta,
  directionRoute,
  presentRoute,
  children,
}: {
  ref?: string;
  directionTitle?: string;
  title: string;
  subnodeType?: string;
  onClose: () => void;
  cta?: { label: string; description?: string; href?: string };
  directionRoute?: string;
  presentRoute?: string;
  children: React.ReactNode;
}) {
  return (
    <>
      <button
        type="button"
        aria-label="Закрыть панель"
        onClick={onClose}
        className="fixed inset-0 z-30 bg-black/60 lg:hidden"
      />
      <aside className="fixed inset-y-0 right-0 z-40 flex h-full w-full max-w-lg flex-col border-l border-[var(--border-subtle)] bg-[var(--bg-panel)] lg:static lg:max-w-[480px] lg:shrink-0">
        <header className="border-b border-[var(--border-subtle)] px-8 py-8">
          <div className="flex items-start justify-between gap-4">
            <div>
              <p className="font-mono text-[10px] tracking-[0.25em] text-[var(--text-dim)] uppercase">
                Diagnostic Dossier
              </p>
              {dirRef && (
                <p className="mt-2 font-mono text-[11px] tracking-[0.22em] text-[var(--accent-signal)] uppercase">
                  {dirRef}
                  {directionTitle && (
                    <span className="text-[var(--text-dim)]">
                      {" "}
                      · {directionTitle}
                    </span>
                  )}
                </p>
              )}
              {subnodeType && (
                <p className="mt-1 font-mono text-[9px] tracking-[0.18em] text-[var(--text-dim)] uppercase">
                  {subnodeType}
                </p>
              )}
              <h2 className="mt-2 text-2xl font-semibold leading-tight tracking-[-0.02em] text-[var(--text-primary)] uppercase">
                {title}
              </h2>
            </div>
            <button
              type="button"
              onClick={onClose}
              aria-label="Закрыть"
              className="font-mono text-2xl leading-none text-[var(--text-dim)] hover:text-[var(--text-primary)]"
            >
              ×
            </button>
          </div>
        </header>

        <div className="flex-1 overflow-y-auto px-8 py-8">{children}</div>

        <footer className="space-y-3 border-t border-[var(--border-subtle)] px-8 py-8">
          {cta && (
            <div>
              <a
                href={cta.href ?? "#"}
                className="flex w-full items-center justify-center border border-[var(--accent-signal)] bg-[var(--accent-signal)] px-6 py-4 font-mono text-[11px] font-medium tracking-[0.2em] text-[var(--bg-deck)] uppercase transition-opacity hover:opacity-90"
              >
                {cta.label}
              </a>
              {cta.description && (
                <p className="mt-4 text-sm leading-relaxed text-[var(--text-muted)]">
                  {cta.description}
                </p>
              )}
            </div>
          )}
          {directionRoute && (
            <Link
              href={directionRoute}
              className="flex w-full items-center justify-center border border-[var(--border-subtle)] px-6 py-3 font-mono text-[11px] tracking-widest text-[var(--text-muted)] uppercase hover:border-[var(--border-edge)] hover:text-[var(--text-primary)]"
            >
              Открыть recovery module
            </Link>
          )}
          {presentRoute && (
            <Link
              href={presentRoute}
              className="flex w-full items-center justify-center px-6 py-3 font-mono text-[11px] tracking-widest text-[var(--text-dim)] uppercase hover:text-[var(--accent-signal)]"
            >
              Present Mode →
            </Link>
          )}
        </footer>
      </aside>
    </>
  );
}

function Section({
  title,
  children,
}: {
  title: string;
  children: React.ReactNode;
}) {
  return (
    <section className="mt-10">
      <h3 className="flex items-center gap-3 font-mono text-[11px] tracking-[0.22em] text-[var(--text-dim)] uppercase">
        <span className="h-px w-6 bg-[var(--accent-signal)]" />
        {title}
      </h3>
      <div className="mt-5">{children}</div>
    </section>
  );
}
