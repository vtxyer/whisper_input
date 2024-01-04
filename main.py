import multiprocessing
from audio_recorder import AudioRecorder
from keyboard_listener import KeyboardListener
from multiprocessing_handler import MultiprocessingHandler

def main():
    # Create a shared buffer for audio data
    buffer = multiprocessing.Array('b', 5 * 1024 * 1024)  # 5MB buffer

    # Create instances of AudioRecorder and KeyboardListener
    audio_recorder = AudioRecorder(buffer)
    keyboard_listener = KeyboardListener()

    # Create a MultiprocessingHandler to manage the processes
    multiprocessing_handler = MultiprocessingHandler()

    # Start the audio recording and keyboard listening processes
    multiprocessing_handler.start_process(audio_recorder.record)
    multiprocessing_handler.start_process(keyboard_listener.listen)

    try:
        while True:
            # Wait for the start_recording event
            keyboard_listener.start_recording.wait()
            print("Start recording")
            audio_recorder.start_recording()

            # Wait for the stop_recording event
            keyboard_listener.stop_recording.wait()
            print("Stop recording")
            audio_recorder.stop_recording()

            # Reset the audio recorder
            audio_recorder.reset()

            # Rotate the buffer if it's full
            if audio_recorder.buffer_full:
                audio_recorder.rotate_buffer()

    except KeyboardInterrupt:
        # Stop all processes when the program is terminated
        multiprocessing_handler.stop_all_processes()

if __name__ == "__main__":
    main()
