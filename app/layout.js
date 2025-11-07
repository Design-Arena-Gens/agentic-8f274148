export const metadata = {
  title: 'PHP Programming Project PDF',
  description: 'Download PHP Programming Project Report',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body style={{ margin: 0, padding: 0 }}>{children}</body>
    </html>
  )
}
