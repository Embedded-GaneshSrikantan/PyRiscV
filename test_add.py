from InstructionExecute import InstExecuteRV


def test_add_instruction():
    executor = InstExecuteRV()
    executor.opcode = "ADD"
    executor.a = 5
    executor.b = 6

    result = executor.execute()
    print(f"ADD 5 + 6 = {result}")
    assert result == 11, f"Expected 11, got {result}"


if __name__ == "__main__":
    test_add_instruction()
    print("Add test passed.")
