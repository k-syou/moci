import React, { useState } from 'react';
import {
  Box,
  Button,
  Card,
  CardContent,
  Typography,
  Grid,
  CircularProgress,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
} from '@mui/material';
import axios from 'axios';

const moods = [
  'happy',
  'sad',
  'excited',
  'romantic',
  'scary',
  'thoughtful',
  'nostalgic',
  'energetic',
  'peaceful',
  'funny'
];

const moodLabels = {
  happy: '행복한',
  sad: '슬픈',
  excited: '신나는',
  romantic: '로맨틱한',
  scary: '무서운',
  thoughtful: '생각에 잠기는',
  nostalgic: '향수에 젖는',
  energetic: '활기찬',
  peaceful: '평화로운',
  funny: '웃긴'
};

const MoodSearch = () => {
  const [selectedMood, setSelectedMood] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSearch = async () => {
    if (!selectedMood) {
      setError('기분을 선택해주세요.');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await axios.post('http://localhost:5000/recommend/mood', {
        mood: selectedMood,
      });
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
        기분에 맞는 영화 추천받기
      </Typography>
      <Box sx={{ display: 'flex', gap: 2, mb: 3 }}>
        <FormControl sx={{ minWidth: 200 }}>
          <InputLabel>기분 선택</InputLabel>
          <Select
            value={selectedMood}
            onChange={(e) => setSelectedMood(e.target.value)}
            label="기분 선택"
          >
            {moods.map((mood) => (
              <MenuItem key={mood} value={mood}>
                {moodLabels[mood]}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
        <Button
          variant="contained"
          onClick={handleSearch}
          disabled={loading || !selectedMood}
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

export default MoodSearch; 