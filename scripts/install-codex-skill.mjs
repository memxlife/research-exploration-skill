#!/usr/bin/env node
import { lstat, mkdir, readlink, rm, symlink } from "node:fs/promises";
import { existsSync } from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const packageDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const skillNames = ["research-exploration", "research-final-report"];
const codexHome = process.env.CODEX_HOME || path.join(os.homedir(), ".codex");
const targetRoot = path.join(codexHome, "skills");
const force = process.env.RESEARCH_EXPLORATION_UPDATE_SKILL === "1";

async function getPathStat(targetPath) {
  try {
    return await lstat(targetPath);
  } catch (error) {
    if (error.code === "ENOENT") return null;
    throw error;
  }
}

async function installSkill(skillName) {
  const sourceDir = path.join(packageDir, ".codex", "skills", skillName);
  const targetDir = path.join(targetRoot, skillName);
  if (!existsSync(sourceDir)) return;
  await mkdir(targetRoot, { recursive: true });
  const targetStat = await getPathStat(targetDir);
  if (targetStat) {
    if (targetStat.isSymbolicLink()) {
      const currentTarget = path.resolve(path.dirname(targetDir), await readlink(targetDir));
      if (currentTarget === sourceDir) {
        console.log(`[research-exploration-skill] Codex skill already links to source: ${targetDir}`);
        return;
      }
    }
    if (!force) {
      console.log(`[research-exploration-skill] Codex skill already exists: ${targetDir}`);
      console.log("[research-exploration-skill] Set RESEARCH_EXPLORATION_UPDATE_SKILL=1 to replace it with a source link.");
      return;
    }
    await rm(targetDir, { recursive: true, force: true });
  }
  await symlink(sourceDir, targetDir, "dir");
  console.log(`[research-exploration-skill] Linked Codex skill: ${targetDir} -> ${sourceDir}`);
}

async function installSkills() {
  const failures = [];
  for (const skillName of skillNames) {
    try {
      await installSkill(skillName);
    } catch (error) {
      failures.push(`${skillName}: ${error.message}`);
    }
  }
  if (failures.length > 0) {
    throw new Error(failures.join("; "));
  }
}

installSkills().catch((error) => {
  console.error(`[research-exploration-skill] Could not install Codex skill: ${error.message}`);
  process.exitCode = 1;
});
