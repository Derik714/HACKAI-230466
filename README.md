# Customer Inquiry Project

## Description

This project provides a conversational interface for handling customer inquiries using a combination of text and image queries. It's built using Rasa, Uagents, and Requests.

## Setup and Installation

1. Clone the repository:

   ```git clone https://github.com/<your-username>/<your-repo-name>.git```
   
   

2. Install required packages:

       cd <your-repo-name>
       pip install rasa==3.6.13 uagents requests

     
   

## Training the Rasa Model

   

    rasa train

   

## Running the Rasa Components

Open dedicated terminals for each command:

1. Start the Rasa server:

   

       rasa run -m models --enable-api

   

2. Start the Rasa actions:

   

	    rasa run actions

## Important
**You will need your own API KEYS from OpenAI and Bing for this to work**

## Running the Uagents Components

1. Create a virtual environment inside the uagentsdir folder:

   

	    cd uagentsdir
	    python -m venv myenv
	    source myenv/bin/activate

   

2. Install required packages in the virtual environment:

   

	    pip install rasa==3.6.13 uagents requests

   

3. Start the server agent:

   

	    python server_agent.py

   

4. Start the user agent:

  

		python user_agent.py

   

## Interaction

1. Choose query type:

   

> Follow the prompts to select either 1 (text query) or 2 (image query).

2. Ask your question:

   

    

> Type your question or provide an image, and press Enter to get the
> response



## Additional Information

- *Dependencies*: List any specific version requirements for dependencies.
- *Troubleshooting*: Provide common troubleshooting tips or links to relevant resources.
- *Contributing*: Describe guidelines for contributing to the project.
- *License*: Specify the project's license.

You can check out our demonstration video [here](https://drive.google.com/file/d/110-uPnIsrKrNbXlkWBz03ceaI87WMcrv/view?usp=sharing)
<hr/>
<b>Regards, Team HackAI-230466</b>
