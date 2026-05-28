/**
 * Agent Harness Skills plugin for OpenCode.
 *
 * Registers this repository's skills directory so OpenCode can discover the
 * repository harness skills without manual symlinks.
 */

import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export const AgentHarnessSkillsPlugin = async () => {
  const skillsDir = path.resolve(__dirname, '../../skills');

  return {
    config: async (config) => {
      config.skills = config.skills || {};
      config.skills.paths = config.skills.paths || [];
      if (!config.skills.paths.includes(skillsDir)) {
        config.skills.paths.push(skillsDir);
      }
    },
  };
};

export default AgentHarnessSkillsPlugin;
