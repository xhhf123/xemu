#!/usr/bin/env python3
import sys
from pathlib import Path

assert(Path(sys.argv[1]).read_text() == 'stage2\n')
Path(sys.argv[2]).write_text('int main(void){}\n')
