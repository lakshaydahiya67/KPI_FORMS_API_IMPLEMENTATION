# KPA Forms API

Railway forms management system built with FastAPI and PostgreSQL.

## 📋 Assignment Overview

This project implements 2 APIs from the KPA_form_data Postman collection:

1. **GET /api/forms/wheel-specifications** - Retrieve wheel specifications with filters
2. **POST /api/forms/bogie-checksheet** - Create bogie checksheet forms

## 🚀 Tech Stack

- **Backend Framework**: FastAPI 0.115.0
- **Database**: PostgreSQL 15
- **ORM**: SQLAlchemy 2.0.36
- **Validation**: Pydantic 2.10.3
- **Containerization**: Docker Compose
- **Environment Management**: python-dotenv

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8+
- Docker & Docker Compose
- Git

### 1. Clone & Navigate
```bash
git clone https://github.com/lakshaydahiya67/KPI_FORMS_API_IMPLEMENTATION.git
cd KPI_FORMS_API_IMPLEMENTATION
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start PostgreSQL Database
```bash
docker-compose up -d
```

### 4. Configure Environment
Update `.env` file with your database credentials:
```env
DATABASE_URL=postgresql://username:password@localhost:5434/kpa_forms
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_DB=kpa_forms
```

### 5. Run the Application
```bash
python run.py
```

The API will be available at: `http://localhost:8002`

## 📚 API Documentation

### Interactive Documentation
- **Swagger UI**: http://localhost:8002/docs
- **ReDoc**: http://localhost:8002/redoc

### Implemented Endpoints

#### 1. GET /api/forms/wheel-specifications
Retrieve wheel specifications with optional filters.

**Query Parameters:**
- `formNumber` (optional): Filter by form number
- `submittedBy` (optional): Filter by submitter
- `submittedDate` (optional): Filter by submission date (YYYY-MM-DD)

**Example Request:**
```
GET /api/forms/wheel-specifications?formNumber=WHEEL-2025-001
```

**Response:**
```json
{
  "success": true,
  "message": "Filtered wheel specification forms fetched successfully.",
  "data": [
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": {
        "condemningDia": "825 (800-900)",
        "lastShopIssueSize": "837 (800-900)",
        "treadDiameterNew": "915 (900-1000)",
        "wheelGauge": "1600 (+2,-1)"
      }
    }
  ]
}
```

#### 2. POST /api/forms/bogie-checksheet
Create a new bogie checksheet form.

**Request Body:**
```json
{
  "formNumber": "BOGIE-2025-001",
  "inspectionBy": "user_id_456",
  "inspectionDate": "2025-07-03",
  "bogieDetails": {
    "bogieNo": "BG1234",
    "dateOfIOH": "2025-07-01",
    "deficitComponents": "None",
    "incomingDivAndDate": "NR / 2025-06-25",
    "makerYearBuilt": "RDSO/2018"
  },
  "bogieChecksheet": {
    "axleGuide": "Worn",
    "bogieFrameCondition": "Good",
    "bolster": "Good",
    "bolsterSuspensionBracket": "Cracked",
    "lowerSpringSeat": "Good"
  },
  "bmbcChecksheet": {
    "adjustingTube": "DAMAGED",
    "cylinderBody": "WORN OUT",
    "pistonTrunnion": "GOOD",
    "plungerSpring": "GOOD"
  }
}
```

**Response:**
```json
{
  "success": true,
  "message": "Bogie checksheet submitted successfully.",
  "data": {
    "formNumber": "BOGIE-2025-001",
    "inspectionBy": "user_id_456",
    "inspectionDate": "2025-07-03",
    "status": "Saved"
  }
}
```

## 🧪 Testing with Postman

1. Import the collection: `KPA_Forms_API.postman_collection.json`
2. Set the environment variable: `base_url = http://localhost:8002`
3. Test the endpoints:
   - Health check: GET /
   - Get wheel specifications (with/without filters)
   - Create wheel specification
   - Create bogie checksheet

## 📁 Project Structure

```
july_14/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── api.py
│   │       └── endpoints/
│   │           └── forms.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── database.py
│   │   └── models.py
│   ├── schemas/
│   │   ├── bogie_checksheet.py
│   │   └── wheel_specification.py
│   └── main.py
├── docker-compose.yml
├── requirements.txt
├── run.py
├── .env
└── README.md
```

## ✨ Key Features Implemented

### Input Validation
- Required field validation using Pydantic
- Date format validation (YYYY-MM-DD)
- Duplicate form number prevention
- Type checking for all fields

### Database Design
- Normalized PostgreSQL schema
- Proper indexing on form numbers
- Timestamp tracking (created_at, updated_at)
- Foreign key relationships

### API Design
- RESTful endpoints matching original specification
- Consistent response format
- Proper HTTP status codes
- CORS enabled for frontend integration

### Environment Configuration
- Environment-based configuration using .env
- Docker Compose for easy database setup
- Development vs production settings

## 🔧 Development Features

### Auto-generated Documentation
FastAPI automatically generates:
- OpenAPI 3.0 specification
- Interactive API documentation
- Request/response schema validation

### Database Migrations
Ready for Alembic integration for database versioning.

### Error Handling
- Comprehensive error responses
- Input validation errors
- Database constraint violations
- HTTP exception handling

## 📊 Database Schema

### WheelSpecification Table
- Primary key: `id`
- Unique constraint: `form_number`
- Technical specification fields
- Audit timestamps

### BogieChecksheet Table
- Primary key: `id`
- Unique constraint: `form_number`
- Nested form sections (bogie details, checksheet, BMBC)
- Inspection tracking

## 🚀 Deployment Notes

### Production Considerations
- Update database credentials in .env
- Configure CORS origins for specific domains
- Enable HTTPS
- Set up proper logging
- Configure database connection pooling

### Scaling
- Add Redis for caching
- Implement rate limiting
- Add monitoring (Prometheus/Grafana)
- Load balancer for multiple instances

## 📝 Limitations & Assumptions

1. **Authentication**: Not implemented (assumed handled by gateway)
2. **File Uploads**: Not required for these specific endpoints
3. **Pagination**: Basic implementation (can be enhanced)
4. **Audit Logging**: Basic timestamps (can be expanded)
5. **Rate Limiting**: Not implemented (production consideration)

## 🎯 Assignment Requirements Met

✅ **API Selection**: Implemented 2 different APIs (GET + POST)  
✅ **Exact Structure**: Matches Postman collection format  
✅ **PostgreSQL**: Database configured and used  
✅ **FastAPI**: Framework choice as recommended  
✅ **Input Validation**: Required fields and data types  
✅ **Environment Config**: .env file configuration  
✅ **Swagger Integration**: Auto-generated OpenAPI docs  
✅ **Postman Collection**: Updated with working endpoints  
✅ **Error Handling**: Proper status codes and messages  

## 📧 Contact

For any questions or clarifications, please contact: lakshaydahiya67@gmail.com

---

**Generated with FastAPI + PostgreSQL for KPA Forms Management System**