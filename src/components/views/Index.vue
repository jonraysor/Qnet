<template>
  <div class="index">
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

      <div class="btn-bar">
			  <img :class="{'disabled' : !(this.pickedCourse && this.pickedSchool)}" src="@/assets/search-icon.svg" @click="submitSearch()">
      </div>
    </div>
    <div class="text mb-3">
      <kbd>
        Find all your class quiz and test questions here.....
      </kbd>
    </div>


    <div class="pop" v-if="showModal">
      <div class="panel">
        <div class="mb-5">Confirmtion</div>
        <div>
          Adding new {{ this.pickedCourse }} for {{ this.pickedSchool }}
        </div>
        <div class="btn-bar">
          <div class="btn-cancel mr-5">
            cancel
          </div>
          <div class="btn-submit">
            submit
          </div>
        </div>
      </div>
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
      showModal: false,
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
.index {
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
        &.disabled {
          filter: contrast(50%);
          cursor: disabled;
          pointer-events: none;
        }
        &:hover {
          filter: contrast(120%);
        }
      }
    }

    .text {
      kbd {
        width: 100%;
      }
    }
  }
 
  .pop {
    position: absolute;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: #000000aa;
    display: flex;
    justify-content: center;
    align-items: center;
    .panel {
      padding: 13px;
      text-align: left;
      background-color: white;
      border-radius: 3px;
      box-shadow: 1px 1px 3px 0px black;
      width: 300px;

      .btn-bar {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        .btn-submit {
          color: white;
          font-size: 14px;
          padding: 3px;
          background-color: green;
          border-radius: 3px;
        }
        .btn-cancel {
          color: white;
          font-size: 14px;
          padding: 3px;
          background-color: gray;
          border-radius: 3px;
        }
      }
    }
  }
}
</style>
