# Deploying YouFace to AWS App Runner

This guide walks you through deploying your **Flask (YouFace)** app using Docker and AWS App Runner.  
When you’re done, your app will be live at a **public HTTPS URL**.

---

## Step 1: Create an AWS Account

1. Go to [https://aws.amazon.com](https://aws.amazon.com)
2. Click **Create an AWS Account**
3. AWS may require a credit card for verification,  
   but App Runner and ECR are covered by the **AWS Free Tier** for this class project.
4. Once your account is ready, open the **AWS Management Console**.

---

## Step 2: Verify Your Project Files

Your project folder (for example, `youface/`) should contain at least:

**Dockerfile**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PORT=5005
EXPOSE 5005
CMD ["python3", "youface.py"]
```

**youface.py**

Ensure your youface program has THIS at the bottom part of your youface.py program. 

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=False, use_reloader=False, threaded=True)
```

---

## Step 3: Build the Docker Image for AWS

### Why
AWS App Runner uses **x86_64 (amd64)** processors so we need to explicitly build for amd64.

### Build Command
Run this from your project directory:
```bash
docker buildx build --platform linux/amd64 -t youface:latest --load .
```

If you get an error that says “no builder instance,” run this once first:
```bash
docker buildx create --name mybuilder --use
docker buildx inspect --bootstrap
```
Then re-run the build command above.

---

## Step 4: Test Locally

Run the container on your computer. It might complain about architecture differences, but it should run:
```bash
docker run --rm -p 5005:5005 youface:latest
```

Visit [http://localhost:5005](http://localhost:5005) in your browser.  
If you see your Flask app, it’s working!  
Stop the container with **Ctrl + C**.

---

## Step 5: Create an ECR Repository

1. In the AWS Console, search for **ECR** (Elastic Container Registry).
2. Click **Create Repository**.
3. Name it **youface** or whatever you want your project to be called.
4. Leave all other settings as defaults.
5. Click **Create**.

You’ll now see your empty ECR repository listed as:
```
<account-id>.dkr.ecr.us-west-2.amazonaws.com/youface
```

This creates a place to put the image that can be used by other components when we actually want to 'run' the server. We need to put the image that we created locally into the ECR repository.

---

## Step 6: Push the Image to ECR

1. Click on your repository. Then, in your ECR repository, click the **View push commands** button (top right).  
2. Follow the steps shown in the AWS Console by copying and pasting them into your terminal window. 
   ```bash
   # 1. Authenticate Docker to your registry

   # 2. build step **SKIP THIS ONE**
   
   # 3. Tag your image for ECR

   # 4. Push the image
   ```
3. When the push completes, confirm the image appears in your ECR repository with the **latest** tag. You might need to refresh the page.

Now that you have uploaded your docker image, it's time to run it. 

---

## Step 7: Deploy with AWS App Runner

1. In the AWS Console, search for **App Runner** and open it.
2. Click **Create An App Runner Service**.
3. Under **Source**, choose:
   - **Container registry**
   - **Amazon ECR**
4. Next to Container image URI, Click Browse.
5. Select your  **youface** repository and the 'latest' tag.
6. Click **Continue**
7. Scroll down to **Deployment Settings**
8. Choose **CreateNewServiceRole** and the default should be **AppRunnerECRAccessRole** 
9. Click **Next**
10. Add a Service Name. Make it **youface** or whatever your project name is.
11. Set the **Port** to be `5005`
12. Scroll all the way down and click **Next**
12. You'll be presented with a review screen. Ensure the port is 5005 
then scroll the rest of the way and click **Create & Deploy**

App Runner will:
- Pull your image from ECR  
- Run it on AWS infrastructure  
- Give you a **public HTTPS URL**

Deployment usually takes 3–5 minutes.

---

## Step 8: Test Your Live App

When the App Runner service status changes to **Running**,  
copy the **Default domain** URL.  
It will look something like this:
```
https://tekdpjdihv.us-west-2.awsapprunner.com/
```

Open that URL in your browser — your youface app should now be running live on AWS!

---

## ✅ Summary

| Step | Description |
|------|--------------|
| 1 | Create AWS account |
| 2 | Verify Dockerfile & Flask app |
| 3 | Build for linux/amd64 |
| 4 | Test locally |
| 5 | Create ECR repository |
| 6 | Push image using “View push commands” |
| 7 | Create App Runner service |
| 8 | Access your public URL |

---

### Notes

- If App Runner logs show **“exec format error”**, your image was built for ARM instead of AMD64.  
  Re-run Step 3 with:
  ```bash
  docker buildx build --platform linux/amd64 -t youface:latest .
  ```
  Then repeat Steps 6–8.

- You can turn on **Automatic deployments from ECR** in App Runner so each new push redeploys automatically.

---

*End of Guide*
