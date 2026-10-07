"""
Problem statement for Ex2

Run any of the BCC examples from Chapter 2. While the program is running,
use a second terminal window to inspect the loaded program using bpftool.
Here’s an example of what I saw by running the hello-map.py example:
$ bpftool prog show name hello
197: kprobe name hello tag ba73a317e9480a37 gpl
loaded_at 2022-08-22T08:46:22+0000 uid 0
xlated 296B jited 328B memlock 4096B map_ids 65
btf_id 179
pids hello-map.py(2785)


You can also use bpftool prog dump commands to see the bytecode and
machine code versions of those programs.

"""