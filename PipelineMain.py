#this consists of the main pipeline logic for the riscv emulator. It will call the instruction decode and execute modules to perform the required operations


if __name__ == "__main__":
    from InstructionFetch import InstructionFetch
    from InstructionDecode import InstructionDecode

    fetcher = InstructionFetch()
    decoder = InstructionDecode()

    instruction = fetcher.fetch()
    decoder.decode(instruction)
    result = decoder.sendToExecute()
    print(f"Result of execution: {result}")