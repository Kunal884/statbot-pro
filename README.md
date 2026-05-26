# StatBot Pro

An autonomous CSV data analyst agent with a modern React frontend that generates Python code to answer natural language questions about your data.
 
## Features:

- **Modern Web Interface**: Beautiful React frontend with real-time chat interface
- **Autonomous Analysis**: Upload CSV files and ask questions in natural language
- **Self-Correcting Agent**: Automatically retries and fixes code execution errors
- **Secure Sandboxing**: Restricted execution environment with no filesystem access
- **Chart Generation**: Automatic matplotlib visualizations saved as PNG files
- **Real-time Processing**: Stream analysis steps for transparency
- **REST API**: Full API access for programmatic usage
- **Session Management**: Maintain context across multiple questions

## Architecture:

- **Frontend**: React + TypeScript + Vite + shadcn/ui
- **Backend**: FastAPI (Python)
- **Agent Framework**: Custom implementation with LangChain concepts
- **Data Processing**: Pandas DataFrame operations
- **Visualization**: Matplotlib with automatic chart generation
- **Security**: Sandboxed code execution with restricted imports
- **Storage**: Local filesystem with public URLs for charts

## System Status:

**Frontend-Backend Integration**: **FULLY INTEGRATED & CLEAN**
- Modern React frontend with real-time chat interface
- Complete API integration with backend
- Session management working correctly
- File upload and question processing functional
- Chart visualization support
- Error handling and user feedback
- All third-party references removed


**Current Features**:
-  CSV file upload with drag-and-drop interface
-  Real-time data analysis with AI agent
-  Interactive chat interface for questions
-  Automatic chart generation and display
-  Session-based data management
-  Comprehensive error handling
-  Production-ready backend with monitoring
-  Modern UI with shadcn/ui components
-  Clean codebase with no external dependencies

##  Quick Start

### Option 1: Production Deployment:

**Backend (Render)**:
1. Fork this repository
2. Connect to [Render](https://render.com)
3. Create a new Web Service from your repo
4. Set environment variables (see DEPLOYMENT.md)
5. Deploy with `python main.py`

**Frontend (Vercel)**:
1. Connect to [Vercel](https://vercel.com)
2. Set root directory to `frontend`
3. Set `VITE_API_URL` to your Render backend URL
4. Deploy automatically

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.
 
### Option 2: Development Mode (Local):

1. **Setup environment variables:**
```bash
cp .env.example .env
# Edit .env file with your preferred settings
```

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

3. **Install Node.js dependencies:**
```bash
cd frontend
npm install
cd ..
```

4. **Start both servers:**
```bash
# Windows
start-dev.bat

# Linux/Mac
python start-dev.py
```

5. **Access the application:**
- Frontend UI: http://localhost:8080
- Backend API: http://localhost:8001

### Option 2: Manual Setup

1. **Start the backend:**
```bash
python main.py
```

2. **Start the frontend (in another terminal):**
```bash
cd frontend
npm run dev
```

### Option 3: Docker Setup (Production)

1. **Build and run with Docker Compose:**
```bash
docker-compose up --build
```

2. **Access the application:**
```
http://localhost:8000
```

## Usage Examples

### Modern Web Interface
1. Open http://localhost:8080 in your browser
2. Upload a CSV file using the drag-and-drop interface
3. Ask questions in the chat interface like:
   - "What is the correlation between sales and marketing spend?"
   - "Show me the sales trend by region"
   - "Create a scatter plot of price vs quantity"
   - "Which product category has the highest average revenue?"

### Legacy Web Interface
1. Open http://localhost:8001 in your browser
2. Upload a CSV file using the file picker
3. Ask questions like:
   - "What is the correlation between sales and marketing spend?"
   - "Show me the sales trend by region"
   - "Create a scatter plot of price vs quantity"
   - "Which product category has the highest average revenue?"

### API Usage

**Upload CSV:**
```bash
curl -X POST -F "file=@data.csv" http://localhost:8001/upload_csv
```

**Ask Question:**
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"question": "What is the correlation between sales and marketing spend?"}' \
  http://localhost:8001/ask_question
```

**Access Generated Charts:**
```bash
# Charts are available at /static/{chart_name}.png
curl http://localhost:8001/static/chart_abc123.png
```
feat: implement AI-powered CSV analysis system
i
- Added natural language question processing
- Integrated autonomous Python code generation
- Enabled chart visualization support
- Added secure sandbox execution
  
## Security Features:

- **Sandboxed Execution**: Code runs in restricted environment
- **Limited Imports**: Only pandas, numpy, matplotlib, math allowed
- **No File System Access**: Cannot read/write files outside workspace
- **No Shell Commands**: subprocess, os.system blocked
- **Execution Timeout**: Prevents infinite loops
- **Input Validation**: All inputs sanitized and validated


## 🤖 Agent Capabilities

### Autonomous Behavior
- Inspects dataframe schema before analysis
- Generates appropriate Python code based on question intent
- Self-corrects on execution errors (up to 3 retries)
- Automatically determines if visualization is needed
- Provides transparent step-by-step progress

### Supported Analysis Types
- **Statistical Analysis**: Mean, median, correlation, distribution
- **Data Exploration**: Shape, columns, data types, missing values
- **Visualizations**: Histograms, scatter plots, line charts, heatmaps
- **Comparative Analysis**: Group by operations, regional comparisons
- **Trend Analysis**: Time series patterns, rolling averages

### Example Questions
- "What are the summary statistics for all numeric columns?"
- "Show me a correlation matrix heatmap"
- "Plot sales over time with a 3-month rolling average"
- "Which region has the most consistent performance?"
- "Create a box plot showing price distribution by category"
- "Find outliers in the revenue data"

## Agent Intelligence
- Multi-step Reasoning — Break complex questions into sub-tasks automatically
- Confidence Scoring — Show how confident the agent is in each answer
- Fallback Explanation — Plain English explanation when code execution fails
- Context Memory — Remember previous answers to support follow-up questions

- feat(agent): improve AI analysis workflow

- Added intelligent dataset schema detection
  - Automatically identifies numeric, categorical, and datetime columns
  - Improves analysis accuracy for mixed datasets

- Enhanced follow-up question handling
  - Maintains session memory between user queries
  - Supports context-aware analysis responses

- Improved autonomous retry mechanism
  - Detects execution errors automatically
  - Regenerates corrected Python code up to 3 retries

- Added confidence scoring system
  - Displays confidence level for generated insights
  - Helps users evaluate analysis reliability


## 📁 Project Structure

```
statbot-pro/
├── main.py                 # FastAPI server
├── agent.py               # Autonomous agent implementation
├── config.py              # Configuration management
├── monitoring.py          # System monitoring
├── requirements.txt       # Python dependencies
├── start-dev.py           # Development startup script
├── start-dev.bat          # Windows development startup
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
├── frontend/             # React frontend application
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── pages/        # Page components
│   │   ├── lib/          # Utilities and API client
│   │   └── types/        # TypeScript type definitions
│   ├── package.json      # Node.js dependencies
│   └── vite.config.ts    # Vite configuration
├── templates/
│   └── index.html        # Legacy web interface
├── workspace/            # CSV upload directory
├── static/              # Generated charts
├── example_data.csv     # Sample dataset
├── test_examples.py     # Basic API tests
├── advanced_test.py     # Advanced functionality tests
└── README.md           # This file
```

## Testing

### Basic Functionality Test
```bash
python test_examples.py
```

### Advanced Features Test
```bash
python advanced_test.py
```

### Manual Testing
1. Start the server: `python main.py`
2. Open http://localhost:8001
3. Upload `example_data.csv`
4. Try the example questions provided in the interface

## Configuration

### Environment Variables
- `PORT`: Server port (default: 8001)
- `HOST`: Server host (default: 0.0.0.0)
- `WORKSPACE_DIR`: CSV upload directory (default: ./workspace)
- `STATIC_DIR`: Chart output directory (default: ./static)

### Security Settings
The agent's security settings are configured in `agent.py`:
- `ALLOWED_MODULES`: Permitted Python modules
- `BLOCKED_BUILTINS`: Restricted built-in functions
- `timeout`: Code execution timeout (default: 30 seconds)

## Visualization

feat(charts): enhance chart generation and export options

- Added download button for generated charts as PNG
- Closed matplotlib figures explicitly after save to fix memory leak
- Supported histogram, scatter, line, heatmap and box plot generation
- Added copy-to-clipboard button for generated Python code blocks
- Supported exporting full chat conversation as PDF report
- Auto-saved charts as uniquely named PNGs to static directory
- Returned chart URLs in API response for frontend rendering

   feat(visualization): upgrade chart generation system

- Enhanced matplotlib chart rendering
  - Improved chart quality and resolution
  - Added automatic chart titles and labels

- Added advanced visualization support
  - Enabled stacked bar charts and multi-line graphs
  - Improved heatmap readability for large datasets

- Optimized chart memory handling
  - Closed matplotlib figures after export
  - Reduced backend memory consumption

- Improved chart export functionality
  - Supported PNG download for generated charts
  - Added chart preview rendering in frontend

## Production Deployment

### Docker Deployment (Recommended)
```bash
# Build the image
docker build -t statbot-pro .

# Run with custom port
docker run -p 8080:8000 -v $(pwd)/data:/app/workspace statbot-pro
```
## Backend Enhancements

- Caching Layer — Cache repeated queries on same dataset for faster responses
- Async Job Queue — Handle long-running analyses without blocking the API
- Webhook Support — Notify external services when analysis completes
- Rate Limiting — Per-session request throttling to prevent abuse
- CSV Validation — Pre-execution schema validation before agent runs

## Backend/Security

feat(backend): strengthen API security and performance

- Implemented rate limiting on /ask_question to prevent API abuse
- Added backend request logging with response time tracking
- Added CORS headers to /upload_csv for cross-origin support
- Blocked subprocess, os.system and file I/O in sandboxed execution
- Fixed session state persistence across multiple CSV uploads
- Added graceful error handling for CSVs with no numeric columns
- Implemented request debouncing to prevent duplicate submissions
- Added /health endpoint for uptime monitoring and deployment checks

### Security Considerations
- Run behind a reverse proxy (nginx/Apache)
- Enable HTTPS with SSL certificates
- Implement rate limiting
- Add authentication if needed
- Monitor resource usage
- Regular security updates

## API Reference

### Endpoints

#### `POST /upload_csv`
Upload a CSV file for analysis.

**Request:**
- Content-Type: multipart/form-data
- Body: CSV file

**Response:**
```json
{
  "message": "CSV uploaded successfully",
  "filename": "unique_filename.csv",
  "shape": [rows, columns],
  "columns": ["col1", "col2", ...],
  "sample": [{"col1": "val1", ...}, ...]
}
```

#### `POST /ask_question`
Ask a natural language question about the uploaded data.

**Request:**
```json
{
  "question": "What is the correlation between sales and marketing spend?"
}
```

**Response:**
```json
{
  "answer": "Analysis results...",
  "chart_url": "/static/chart_abc123.png",
  "code_used": "Generated Python code",
  "analysis_type": "visualization|computation",
  "dataframe_info": {...}
}
```

#### `GET /static/{image_name}`
Access generated chart images.

#### `GET /health`
Health check endpoint.

## 🐛 Troubleshooting

### Common Issues

**Port Already in Use:**
```bash
# Change port in main.py or use environment variable
PORT=8002 python main.py
```

**Dependencies Issues:**
```bash
# Clean install
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

**Chart Generation Fails:**
- Ensure matplotlib backend is set correctly
- Check static directory permissions
- Verify sufficient disk space

**Memory Issues with Large CSV:**
- Implement chunking for large files
- Add memory monitoring
- Consider using Dask for big data

## Performance Tips

- Use smaller CSV files for faster processing
- Cache frequently used datasets
- Implement connection pooling for high traffic
- Monitor memory usage with large datasets
- Use async processing for multiple request

## Data Preview & Upload

feat(upload): improve CSV upload and data preview experience

- Implemented drag-and-drop file upload with visual drop zone highlight
- Supported CSV preview table with pagination before analysis
- Added summary card showing row count, column count, and null values
- Highlighted missing value percentage per column in data preview
- Displayed dataframe shape and column preview after CSV upload
- Added toast notifications for upload success and error states
- Validated .csv-only file extension restriction on upload endpoint
- Added file size limit check before processing large uploads

**Data & Processing**
- Implemented session-based CSV storage with unique file identifiers
- Added dataframe schema inspection before code generation
- Enabled multi-column statistical aggregations and group-by operations
- Supported time series parsing and rolling window calculations

**Agent & AI**
- Built self-correcting agent loop with up to 3 automatic retries on errors
- Added intent detection to route questions to computation vs. visualization paths
- Injected dataframe context into prompts for schema-aware code generation
- Restricted sandbox to pandas, numpy, matplotlib, and math imports only
- 
**Visualization**
- Auto-saved matplotlib charts as uniquely named PNGs to static directory
- Returned chart URLs in API responses for frontend rendering
- Supported histogram, scatter, line, heatmap, and box plot generation

**API & Backend**
- Exposed REST endpoints for upload, question answering, and chart retrieval
- Added `/health` endpoint for uptime monitoring and deployment checks
- Blocked subprocess, os.system, and file I/O inside sandboxed execution
- Set 30-second execution timeout to prevent runaway code loops

**Frontend**
- Built drag-and-drop CSV upload with instant column/shape preview
- Rendered AI responses and chart images inline in chat thread
- Displayed step-by-step agent progress in real time
- Handled API errors gracefully with user-facing feedback messages

**DevOps**
- Added `docker-compose.yml` for single-command local and production setup
- Included `start-dev.py` and `start-dev.bat` for cross-platform dev startup
- Configured Vite proxy to route frontend API calls to FastAPI backend
- Provided Render + Vercel deployment path with environment variable docs
- 
## Security
- Restrict allowed file extensions to .csv only on upload endpoint
- Add file size limit validation before processing large uploads
- Sanitize column names before injecting into generated code prompts

## Refactor
- Extract sandbox execution logic into dedicated sandbox.py module
- Centralize error messages into constants file for easier localization
- Replace inline API URLs with environment-based config in frontend
- 
##   Bug Fixes

- Fix session state not persisting across multiple CSV uploads
- Resolve matplotlib figure not closing after chart generation causing memory leak
- Fix CORS headers missing on /upload_csv endpoint for cross-origin requests
- Handle edge case where CSV has no numeric columns for statistical analysis


## Maintenance/refactor-focused:

- refactor: modularize sandbox execution and centralize config
- Extract sandboxed code runner into dedicated sandbox.py module
- Centralize error messages into constants.py for localization support
- Replace hardcoded API URLs with VITE_API_URL env variable in frontend
- Add .csv extension whitelist validation on upload route
- Close matplotlib figures explicitly after chart save to fix memory leak

## Feature-focused
feat: enhance StatBot Pro with improved agent reliability and UX

- Add retry logic display in chat for failed code executions
- Improve chart cleanup to prevent matplotlib memory leaks
- Validate CSV column names before code generation prompt injection
- Add file size limit check on upload endpoint
- Fix CORS headers on /upload_csv for cross-origin requests
- Update session state to persist across multiple CSV uploads


## Future Enhancements

- Support for multiple file formats (Excel, JSON, Parquet)
- Advanced ML capabilities (clustering, classification)
- Real-time data streaming support
- Multi-user session management
- Advanced visualization libraries (Plotly, Seaborn)
- Natural language to SQL conversion
- Integration with cloud storage (S3, GCS)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## Recent Updates
- Added deployment configuration files
- Improved production setup documentation
- Added deployment checklist
- Enhanced project structure for cloud deployment

## Challenges Faced
_Python 3.14 incompatible with Pandas 2.1.3 → solved by switching to Python 3.11
-Missing logs/ and static/ directories causing server crash → fixed by creating them
-CORS issues between frontend and backend → resolved with FastAPI CORSMiddleware
-OpenAI API requires billing credits → configured .env with API key

## Future Scope
-Support Excel, JSON, Parquet file formats
-Add user login and saved analysis history
-Integrate free open-source LLM (LLaMA) to remove OpenAI cost
-Deploy on Render (backend) + Vercel (frontend)
-Add PDF export of analysis results
-Multi-user session management

## Key Features of Our Project:
- Easy CSV dataset upload
- Natural language question answering
- AI-generated insights and analysis
- Automatic chart and graph generation
- User-friendly interface with no coding required

## Team Members

- **Kunal Girme** — [github.com/Kunal884](https://github.com/Kunal884)
- **Sreeparna Mukherjee** — [github.com/SreeparnaMukherjee](https://github.com/SreeparnaMukherjee)
- **Sanika Linge** — [github.com/sanikalinge448-rgb ](https://github.com/sanikalinge448-rgb)
---

*Built as part of the Infotact Solutions Internship Program — May 2026*
Test update for Git commit

<!-- Updated: May 24, 2026 -->
