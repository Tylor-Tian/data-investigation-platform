try:
    from pyflink.datastream import StreamExecutionEnvironment
except Exception:  # pragma: no cover - pyflink not installed in tests
    StreamExecutionEnvironment = None


def process_stream(topic: str) -> None:
    """Consume a stream using Flink."""
    if StreamExecutionEnvironment is None:
        raise RuntimeError("pyflink is not available")
    env = StreamExecutionEnvironment.get_execution_environment()
    # Placeholder for actual source; in real use, configure Kafka or other source
    print(f"Processing stream from {topic}")
    env.execute("process_stream")
