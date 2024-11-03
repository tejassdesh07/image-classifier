## Setting Up the Environment

### 1. Set up the virtual environment

#### On Windows:
1. Open a terminal or Command Prompt.
2. Navigate to the project directory:
   ```bash
   cd path/to/image-classifier
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```

#### On macOS:
1. Open a terminal.
2. Navigate to the project directory:
   ```bash
   cd path/to/image-classifier
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

### 2. Install the required libraries
With the virtual environment activated, install the dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

---

### 3. Set up the `.env` file for the OpenAI API key

1. In the project root directory, create a file named `.env`:
   ```bash
   touch .env
   ```
2. Open the `.env` file in a text editor and add your OpenAI API key as follows:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

---

### 4. Run the Classifier Script

Place your images in the `./data/` folder, and then run the classifier:

   ```bash
   python main.py
   ```

This setup will classify the images and move them to either the `./qr_codes/` or `./normal_photos/` folder based on the classification results.