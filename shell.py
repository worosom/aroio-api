import asyncio


async def run(cmd,
              stdout=asyncio.subprocess.PIPE,
              stderr=asyncio.subprocess.PIPE):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=stdout,
        stderr=stderr)

    return proc
