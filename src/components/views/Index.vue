<template>
  <div>
    <div class="mb-5 search-container">
      <search-bar
        placeholder="search the school"
        :options="schools"
        @update="pickedSchool = $event"
        id="schoolsBar" class="mb-1"/>
      <search-bar
        placeholder="search the course"
        :options="courses"
        @update="pickedCourse = $event"
        id="courseBar" class="mb-1"/>
      <!-- <input id="schoolsBar"
        type="text"
        class="mb-1"
        placeholder="Search the school">
			<input id="classBar"
        type="text"
        class="mb-1"
        placeholder="Search the class"> -->
      <div class="btn-bar">
			  <img src="@/assets/search-icon.svg" @click="submitSearch()">
      </div>
    </div>
    <!-- {{ pickedSchool }}<br>{{ pickedCourse }} -->
    <div class="text mb-3">
      <kbd>
        Find all your class quiz and test questions here.....
      </kbd>
    </div>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar';

export default {
  name: 'Index',
  data() {
    return {
      schools: [],
      courses: [],
      pickedSchool: null,
      pickedCourse: null,
    };
  },
  components: {
    SearchBar,
  },
  mounted() {
    // 'http://10.255.139.136:5000'
    let baseurl = '/api'
    this.axios.get(`${baseurl}/readInSchools`).then((response) => {
      this.schools = response.data
    })
    this.axios.get(`${baseurl}/readInCourses`).then((response) => {
      this.courses = response.data
    })
  },
  methods: {
    submitSearch() {
      alert(`${this.pickedSchool},${this.pickedCourse}`);
    }
  }
};
</script>

<style lang="scss" scoped>
.search-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 100%;

  > input {
    width: 100%;
    height: 100%;
  }

  .btn-bar {
    width: 100%;
    display: flex;
    justify-content: flex-end;
    align-items: flex-end;
    > img {
      cursor: pointer;
      width: 60px;
      height: 30px;
      // height: 100%;
      background-color: darkorange;
      border-radius: 5px;
      transition: all 0.3s;
    }
  }

  .text {
    kbd {
      width: 100%;
    }
  }
}

.search-container:hover > img {
  filter: contrast(200%);
}
</style>
