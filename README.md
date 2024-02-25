# bp_inspector

Untyped Chat Completion Response Format

```
    ChatCompletion(id='chatcmpl-595', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='\nIn Elixir, you can spawn a process using the `spawn` function. For example:\n```\npid = spawn(fn() -> IO.puts("Hello from my new process!") end)\nsend pid, "Hello from the other side!"\n```\nThis will create a new process that executes the given anonymous function and send it a message with the content `"Hello from the other side!"`.\n\nNote that you can also use `spawn` to spawn a process from another process. In this case, the child process is created when the parent process receives the spawn message.', role='assistant', function_call=None, tool_calls=None))], created=1708892433, model='codellama', object='chat.completion', system_fingerprint='fp_ollama', usage=CompletionUsage(completion_tokens=127, prompt_tokens=90, total_tokens=217))
```