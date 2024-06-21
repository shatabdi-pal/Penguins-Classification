import subprocess

def lambda_handler(event, context):
    try:
        # Run the app.py script
        result = subprocess.run(['python3', 'app.py'], capture_output=True, text=True)
        
        # Check if the script ran successfully
        if result.returncode == 0:
            return {
                'statusCode': 200,
                'body': result.stdout
            }
        else:
            return {
                'statusCode': 500,
                'body': f"Error running app.py: {result.stderr}"
            }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
