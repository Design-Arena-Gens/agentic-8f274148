'use client';

export default function Home() {
  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      fontFamily: 'system-ui, -apple-system, sans-serif',
      padding: '20px'
    }}>
      <div style={{
        background: 'white',
        borderRadius: '20px',
        padding: '50px',
        boxShadow: '0 20px 60px rgba(0,0,0,0.3)',
        textAlign: 'center',
        maxWidth: '600px',
        width: '100%'
      }}>
        <div style={{
          fontSize: '60px',
          marginBottom: '20px'
        }}>
          📄
        </div>

        <h1 style={{
          fontSize: '32px',
          color: '#2c3e50',
          marginBottom: '15px',
          fontWeight: '700'
        }}>
          PHP Programming Project
        </h1>

        <p style={{
          fontSize: '18px',
          color: '#7f8c8d',
          marginBottom: '35px',
          lineHeight: '1.6'
        }}>
          Complete project report with two PHP tasks:<br/>
          • Find Largest of Three Numbers<br/>
          • Reverse String using strrev()
        </p>

        <a
          href="/PHP_Programming_Project.pdf"
          download
          style={{
            display: 'inline-block',
            background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            color: 'white',
            padding: '18px 45px',
            borderRadius: '50px',
            textDecoration: 'none',
            fontSize: '18px',
            fontWeight: '600',
            boxShadow: '0 10px 30px rgba(102, 126, 234, 0.4)',
            transition: 'all 0.3s ease',
            cursor: 'pointer'
          }}
          onMouseOver={(e) => {
            e.target.style.transform = 'translateY(-2px)';
            e.target.style.boxShadow = '0 15px 40px rgba(102, 126, 234, 0.5)';
          }}
          onMouseOut={(e) => {
            e.target.style.transform = 'translateY(0)';
            e.target.style.boxShadow = '0 10px 30px rgba(102, 126, 234, 0.4)';
          }}
        >
          ⬇️ Download PDF Report
        </a>

        <div style={{
          marginTop: '35px',
          padding: '20px',
          background: '#f8f9fa',
          borderRadius: '10px',
          fontSize: '14px',
          color: '#6c757d'
        }}>
          <strong>Includes:</strong> Front page, Task descriptions, AIM, Problem statements,
          Constraints, Procedures, Programs, Outputs, and Conclusions
        </div>
      </div>
    </div>
  );
}
