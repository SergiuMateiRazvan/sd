import React from 'react';
import {useState, useEffect} from 'react';
import {InternshipList} from './InternshipList';
import {getInternships} from '../../service';
import {SearchBar} from './SearchBar';
import {Sort} from './Sort';
import {Filter} from './Filter';
import {HeaderNav} from '../common/HeaderNav';

export const Home = () => {
  const [internshipsList, setInternshipList] = useState([]);


  useEffect(() => {
    getInternships().then((response) => {
      setInternshipList(response);
    });
  }, []);

  const onSearch = (searchText) => {
    getInternships({title: searchText}).then((response) =>
      setInternshipList(response),
    );
  };

  const onSort = (sortField, sortDirection='ascending') => {
    getInternships({}, {sort: sortField, sort_direction: sortDirection})
        .then((response) => setInternshipList(response));
  };

  const onFilter = (location, date) => {
    const filters = {};
    if (location) {
      filters.location = location;
    }
    if (date) {
      filters.date = date;
    }
    getInternships(filters, {})
        .then((response) => setInternshipList(response));
  };

  return (
    <div className={'outerWrapper'}>
      <HeaderNav />
      <Sort onSort={onSort} />
      <Filter onFilter={onFilter} />
      <SearchBar onSearch={onSearch} />
      <InternshipList internships={internshipsList}/>
    </div>
  );
};
