# Delegate & Event system in C#

C# developers are familiar with `delegate` and `event` as core mechanisms for implementing callbacks. This article examines few aspects of their design and usage.

## The Default Multicast Delegate Behavior

The `delegate` keyword implicitly creates a `MulticastDelegate`, as seen in the `Action` type declaration:

```c#
public delegate void Action();
```

This allows unrestricted `+=`/`-=` operations:

```c#
public Action action;
...
action += () => {...}
...
action.Invoke();
```

Concerns with this design:

- **Single-handler enforcement**: Scenarios requiring exclusive single handler assignment necessitate additional validation code.
- **Readonly limitations**: Readonly delegates can only be initialized in constructors, which are often impractical.

Consideration: Non-multicast delegates should be the default for general-purpose delegates, reserving multicast behavior specifically for event handling scenarios.

## Synchronous vs. Asynchronous Execution

While the C# team considers `async void` acceptable in event contexts, this introduces ambiguity:

- **Synchronous handlers** execute sequentially and block the thread until completion.
- **Async handlers** (`async void`) synchronously run until the first `await`, then yield execution to subsequent handlers, leaving remaining async operations in background threads.

Thus, `MulticastDelegate.Invoke()` **cannot guarantee full handler execution completion**. Consider this example:

```c#
// Problematic even with Task return type
Func<Task> func = async () => { await Task.Delay(1000); };
func += () => Task.CompletedTask;

await func(); // Only awaits final handler
```

**Common Workarounds and Their Limitations**:

1. **`Task.WhenAll` pattern**:

   ```c#
   var tasks = func.GetInvocationList().Cast<Func<Task>>().Select(h => h());
   await Task.WhenAll(tasks);
   ```

   - Requires significant refactoring from `Action` to `Func<Task>`
   - Violates the event pattern principle where publishers shouldn't manage subscriber execution

2. **Error handling challenges**:
   While `async void` allows try-catch in handlers, this depends on consistent implementation across all team members.

3. **Core Issue**:
   The current multicast implementation conflicts with the recommended "fire-and-forget" event model:

   - Synchronous handlers block execution
   - Async handlers exhibit partial synchronous execution

## AsyncEventHandler Implementations

Though not native to .NET Core, various implementations address asynchronous events:

- **Microsoft's Event-based Asynchronous Pattern**
  [Implementing the Event-based Asynchronous Pattern](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/implementing-the-event-based-asynchronous-pattern)
- **Community Solutions**
  - [AsyncFuncExtension](https://gist.github.com/idea-lei/69a6fe397dea76ff3d4c9e1399addaa1)
  - [AsyncEvent](https://github.com/TAGC/AsyncEvent)
  - `Microsoft.VisualStudio.Threading.AsyncEventHandler` (Visual Studio SDK)

