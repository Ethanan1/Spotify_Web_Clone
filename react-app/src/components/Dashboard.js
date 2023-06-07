import React, { useContext, useEffect, useState } from 'react';
import { AuthContext } from '../contexts/AuthContext';
import { useHistory } from 'react-router-dom';
import axios from 'axios';

const Dashboard = () => {
  const { user, isAuthenticated, logout } = useContext(AuthContext);
  const [playlists, setPlaylists] = useState([]);
  const [newPlaylistName, setNewPlaylistName] = useState('');
  const [editPlaylistName, setEditPlaylistName] = useState('');
  const [editPlaylistId, setEditPlaylistId] = useState('');
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [favorites, setFavorites] = useState([]);
  const [selectedPlaylistId, setSelectedPlaylistId] = useState('');
  const history = useHistory();

  useEffect(() => {
    if (isAuthenticated && user) {
      fetchPlaylists();
      fetchFavorites();
    }
  }, [isAuthenticated, user]);

  const fetchPlaylists = async () => {
    try {
      const response = await axios.get('/api/playlists');
      const playlistsData = response.data.playlists;
      setPlaylists(playlistsData);
    } catch (error) {
      console.error('Failed to fetch playlists:', error);
    }
  };

  const fetchFavorites = async () => {
    try {
      const response = await axios.get('/api/favorites');
      const favoritesData = response.data.favorites;
      setFavorites(favoritesData);
    } catch (error) {
      console.error('Failed to fetch favorites:', error);
    }
  };

  const addPlaylist = async () => {
    try {
      const response = await axios.post('/api/playlists', {
        name: newPlaylistName,
      });
      const newPlaylist = response.data;
      setPlaylists([...playlists, newPlaylist]);
      setNewPlaylistName('');
    } catch (error) {
      console.error('Failed to add playlist:', error);
    }
  };

  const editPlaylist = async () => {
    try {
      await axios.put(`/api/playlists/${editPlaylistId}`, {
        name: editPlaylistName,
      });
      const updatedPlaylists = playlists.map((playlist) =>
        playlist.id === editPlaylistId ? { ...playlist, name: editPlaylistName } : playlist
      );
      setPlaylists(updatedPlaylists);
      setEditPlaylistId('');
      setEditPlaylistName('');
    } catch (error) {
      console.error('Failed to edit playlist:', error);
    }
  };

  const deletePlaylist = async (playlistId) => {
    try {
      await axios.delete(`/api/playlists/${playlistId}`);
      const updatedPlaylists = playlists.filter((playlist) => playlist.id !== playlistId);
      setPlaylists(updatedPlaylists);
    } catch (error) {
      console.error('Failed to delete playlist:', error);
    }
  };

  const handleSearch = async () => {
    try {
      const response = await axios.get(`/api/songs?q=${searchQuery}`);
      const searchResultsData = response.data.songs;
      setSearchResults(searchResultsData);
      history.push(`/search?query=${searchQuery}`);
    } catch (error) {
      console.error('Failed to search for songs:', error);
    }
  };

  const handleAddToPlaylist = async (song) => {
    try {
      await axios.post(`/api/playlists/${selectedPlaylistId}/songs`, { song_id: song.id });
      await fetchPlaylists();
    } catch (error) {
      console.error('Failed to add song to playlist:', error);
    }
  };

  const handleAddToFavorites = async (song) => {
    try {
      await axios.post('/api/favorites', { song_id: song.id });
      fetchFavorites();
    } catch (error) {
      console.error('Failed to add song to favorites:', error);
    }
  };

  const handleRemoveFromFavorites = async (favoriteId) => {
    try {
      await axios.delete(`/api/favorites/${favoriteId}`);
      fetchFavorites();
    } catch (error) {
      console.error('Failed to remove song from favorites:', error);
    }
  };

  return (
    <div>
      <h1>Welcome to your Dashboard, {user.username}!</h1>
      <button onClick={logout}>Logout</button>

      <h2>Playlists</h2>
      <input
        type="text"
        value={newPlaylistName}
        onChange={(e) => setNewPlaylistName(e.target.value)}
        placeholder="New playlist name"
      />
      <button onClick={addPlaylist}>Add Playlist</button>

      {playlists.map((playlist) => (
        <div key={playlist.id}>
          <h3>{playlist.name}</h3>
          <button onClick={() => setEditPlaylistId(playlist.id)}>Edit</button>
          <button onClick={() => deletePlaylist(playlist.id)}>Delete</button>
        </div>
      ))}

      {editPlaylistId && (
        <div>
          <input
            type="text"
            value={editPlaylistName}
            onChange={(e) => setEditPlaylistName(e.target.value)}
            placeholder="Edit playlist name"
          />
          <button onClick={editPlaylist}>Save</button>
        </div>
      )}

      <h2>Search Songs</h2>
      <input
        type="text"
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
        placeholder="Search songs"
      />
      <button onClick={handleSearch}>Search</button>

      {searchResults.map((song) => (
        <div key={song.id}>
          <h3>{song.title}</h3>
          <p>{song.artist}</p>
          <button onClick={() => handleAddToPlaylist(song)}>Add to Playlist</button>
          <button onClick={() => handleAddToFavorites(song)}>Add to Favorites</button>
        </div>
      ))}

      <h2>Favorites</h2>
      {favorites.map((favorite) => (
        <div key={favorite.id}>
          <h3>{favorite.song.title}</h3>
          <p>{favorite.song.artist}</p>
          <button onClick={() => handleAddToPlaylist(favorite.song)}>Add to Playlist</button>
          <button onClick={() => handleRemoveFromFavorites(favorite.id)}>Remove from Favorites</button>
        </div>
      ))}
    </div>
  );
};

export default Dashboard;
