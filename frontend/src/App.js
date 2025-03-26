import React from 'react';
import { Container, Typography, Box, CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import MovieSearch from './components/MovieSearch';
import GenreSearch from './components/GenreSearch';
import MoodSearch from './components/MoodSearch';

const theme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#90caf9',
    },
    secondary: {
      main: '#f48fb1',
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="lg">
        <Box sx={{ my: 4 }}>
          <Typography variant="h3" component="h1" gutterBottom align="center">
            영화 추천 시스템
          </Typography>
          <MovieSearch />
          <Box sx={{ my: 4 }} />
          <GenreSearch />
          <Box sx={{ my: 4 }} />
          <MoodSearch />
        </Box>
      </Container>
    </ThemeProvider>
  );
}

export default App; 