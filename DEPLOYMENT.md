# Deploying to Vercel

## Prerequisites
- Vercel account (free tier works)
- Google Gemini API key

## Deployment Steps

### 1. Install Vercel CLI (optional)
```bash
npm install -g vercel
```

### 2. Deploy via GitHub (Recommended)

1. Push your code to GitHub (already done)
2. Go to [vercel.com](https://vercel.com)
3. Click "Add New Project"
4. Import your GitHub repository: `redeyessssss/infoai`
5. Configure project:
   - Framework Preset: **Other**
   - Root Directory: `./`
   - Build Command: (leave empty)
   - Output Directory: `frontend`

### 3. Add Environment Variables

In Vercel project settings, add:
- **Name:** `GEMINI_API_KEY`
- **Value:** Your Google Gemini API key
- **Environment:** Production, Preview, Development

### 4. Deploy

Click "Deploy" and wait for deployment to complete.

### 5. Test

Visit your deployed URL (e.g., `https://infoai.vercel.app`)

## Alternative: Deploy via CLI

```bash
# Login to Vercel
vercel login

# Deploy
vercel

# Add environment variable
vercel env add GEMINI_API_KEY

# Deploy to production
vercel --prod
```

## Important Notes

1. **Serverless Functions**: The backend runs as Vercel serverless functions
2. **Cold Starts**: First request may be slower (serverless cold start)
3. **File Size Limits**: Vercel has a 4.5MB limit for serverless functions
4. **Execution Time**: 10 seconds max for free tier
5. **API Key Security**: Never commit `.env` file to GitHub

## Troubleshooting

### Build Fails
- Check that `requirements.txt` is in the root directory
- Verify all Python dependencies are compatible with Vercel

### API Not Working
- Ensure `GEMINI_API_KEY` environment variable is set
- Check Vercel function logs for errors

### CORS Issues
- The app is configured to allow all origins
- If issues persist, check Vercel function logs

## Custom Domain (Optional)

1. Go to Project Settings → Domains
2. Add your custom domain
3. Follow DNS configuration instructions

## Monitoring

- View logs: Vercel Dashboard → Your Project → Functions
- Monitor usage: Vercel Dashboard → Usage

## Cost

- Free tier includes:
  - 100GB bandwidth
  - 100 serverless function executions per day
  - Unlimited static hosting

For higher usage, upgrade to Pro plan.
