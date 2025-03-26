import React, { useState } from 'react';
import {
  Box,
  Button,
  Card,
  CardContent,
  Typography,
  CircularProgress,
  FormGroup,
  FormControlLabel,
  Checkbox,
} from '@mui/material';
import Grid from '@mui/material/Grid';
import axios from 'axios';

const genres = [
  'Action',
  'Adventure',
  'Animation',
  'Children',
  'Comedy',
  'Crime',
  'Documentary',
  'Drama',
  'Fantasy',
  'Film-Noir',
  'Horror',
  'Musical',
  'Mystery',
  'Romance',
  'Sci-Fi',
  'Thriller',
  'War',
  'Western',
];

const GenreSearch = () => {
  const [selectedGenres, setSelectedGenres] = useState([]);
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleGenreChange = (genre) => {
    setSelectedGenres((prev) =>
      prev.includes(genre)
        ? prev.filter((g) => g !== genre)
        : [...prev, genre]
    );
  };

  const handleSearch = async () => {
    if (selectedGenres.length === 0) {
      setError('최소 하나의 장르를 선택해주세요.');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await axios.post('http://localhost:5000/recommend/genre', {
        genres: selectedGenres,
      });
      console.log(response.data);
      setResults(response.data);
    } catch (err) {
      setError(err.response?.data?.error || '검색 중 오류가 발생했습니다.');
      setResults([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box>
      <Typography variant="h5" gutterBottom>
        장르로 추천받기
      </Typography>
      <FormGroup row sx={{ mb: 3, flexWrap: 'wrap', gap: 1 }}>
        {genres.map((genre) => (
          <FormControlLabel
            key={genre}
            control={
              <Checkbox
                checked={selectedGenres.includes(genre)}
                onChange={() => handleGenreChange(genre)}
                color="primary"
              />
            }
            label={genre}
          />
        ))}
      </FormGroup>
      <Box sx={{ display: 'flex', gap: 2, mb: 3 }}>
        <Button
          variant="contained"
          onClick={handleSearch}
          disabled={loading || selectedGenres.length === 0}
          sx={{ minWidth: '120px' }}
        >
          {loading ? <CircularProgress size={24} /> : '검색'}
        </Button>
      </Box>
      {error && (
        <Typography color="error" sx={{ mb: 2 }}>
          {error}
        </Typography>
      )}

      {results.length > 0 && (
        <Grid container spacing={2}>
          {results.map((movie, index) => (
            <Grid item xs={12} sm={6} md={4} key={index}>
              <Card>
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    {movie.title}
                  </Typography>
                  <Typography color="textSecondary">
                    개봉일: {movie.release_date}
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      )}
    </Box>
  );
};

export default GenreSearch; 