// News-image entry (Node 22, standard library only): the entry image is
// entry.png beside this file, and the program copies it to /output/entry.png.
// The image sums up the world's news of Thursday 19 November 2026 as a
// newspaper front page drawn by draw.py (see that file for the generator).
// The copy is byte for byte, so two runs of this program write the same bytes.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
